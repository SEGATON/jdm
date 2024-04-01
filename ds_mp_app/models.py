from django.db import models
from django.conf import settings
# Create your models here.
from ecommerce.models import Product, TaxSettings,TaxRate,Address, Payment

class DropshipFeeSettings(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)

	dropship_fee_rate = models.DecimalField(max_digits=9, decimal_places=2)

class OrderItem(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='ds_mp_order_item_user')

	order_item = models.ForeignKey(Product,on_delete=models.CASCADE, null=True, blank=True, related_name='ds_mp_order_item')
	order_item_quantity = models.IntegerField(default=1,null=True, blank=True)


	def __str__(self):
		return self.order_item.title

	def get_total_item_price(self):
		if self.order_item.price_sale:
			return self.order_item_quantity * self.order_item.price_sale
		elif self.order_item.price_regular:
			return self.order_item_quantity * self.order_item.price_regular

	def total_order_items_weight(self):

		total_order_items_weight = self.order_item_quantity * self.order_item.item_weight_value

		return total_order_items_weight


class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='ds_mp_order')

	order_number = models.CharField(max_length=13, null=True, blank=True,)
	order_items = models.ManyToManyField(OrderItem,null=True, blank=True)
	
	date_created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
	date_updated = models.DateTimeField(auto_now_add=True,null=True, blank=True)

	tax_rate = models.ForeignKey(TaxRate,on_delete=models.CASCADE, null=True, blank=True )

	dropship_fee = models.ForeignKey(DropshipFeeSettings, on_delete=models.CASCADE, null=True, blank=True)

	refund_requested = models.BooleanField(default=False, null=True,blank=True)
	refund_requested_accepted = models.BooleanField(default=False, null=True,blank=True)
	refund_requested_proccessed = models.BooleanField(default=False, null=True,blank=True)

	billing_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True, related_name='billing_address_ds_mp')
	shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True, related_name='shipping_address_ds_mp')

	payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True, related_name='payment_ds_mp')


	def get_sub_total(self):
		total = 0

		for order_item in self.order_items.all():
			total += order_item.get_total_item_price()

		return total

	def add_dropship_fee(self):
		dropship_fee_rate = self.dropship_fee.dropship_fee_rate

		return dropship_fee_rate



	def calculate_tax_rate(self):


		tax_rate = self.tax_rate.tax_rate_amount

		calculate_tax_rate = None

		return tax_rate

	
	def get_grand_total(self):
		grand_total = self.get_sub_total() + self.calculate_tax_rate() + self.add_dropship_fee()

		return grand_total









class Refunds(models.Model):
	REFUND_REQUEST_STATUS = (
		('submitted','Submitted'),
		('pending','Pending'),
		('approved','Approved'),
		('rejected','Rejected'),
	)
	refund_request_status = models.CharField(max_length=50, choices=REFUND_REQUEST_STATUS)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True,blank=True, related_name='refund_for_user_ds_mp')
	order = models.ForeignKey('Order',on_delete=models.CASCADE, null=True,blank=True)

	reason_for_refund = models.TextField(max_length=300,null=True,blank=True )

	refund_accepted = models.BooleanField(default=False)

	date_requested = models.DateTimeField(auto_now_add=True)









































