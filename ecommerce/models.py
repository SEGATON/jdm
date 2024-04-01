from django.db import models
from django.urls import reverse
from django.conf import settings
from ckeditor.fields import RichTextField

from localflavor.us.models import USStateField
from localflavor.us.models import USZipCodeField
from localflavor.us.models import USPostalCodeField
from localflavor.us.models import USSocialSecurityNumberField

from django.utils.translation import gettext_lazy as _ 
from accounts.models import CustomUser
from colorfield.fields import ColorField
from mptt.models import MPTTModel, TreeForeignKey

class TaxRate(models.Model):
	state = USStateField()
	tax_rate_amount = models.DecimalField(max_digits=9, decimal_places=2)

	def __str__(self):
		return self.state

	def get_tax_rate_percentage(self):
		tax_rate_percentage = 'go fuck yourself'
		return tax_rate_percentage
		
class TaxSettings(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)

	tax_rate = models.ForeignKey(TaxRate, on_delete=models.CASCADE,null=True,blank=True)

	def __str__(self):
		return self.title

class ProductSize(models.Model):
	SIZE_LABEL = {
		('cm','CM'),
		('in','Inches'),
		('ft','Feet'),
	
	}

	SIZES = {
		('xxxs','XXXS'),('xxs','XXS'),('xs','XS'),
		('s','S'),('m','M'),('l','L'),('xl','XL'),
		('xxl','XXL'),('xxxl','XXXL'),
	}

	size = models.CharField(choices=SIZES,max_length=90,null=True,blank=True)
	size_value_h = models.DecimalField(max_digits=9, decimal_places=2)
	size_value_l = models.DecimalField(max_digits=9, decimal_places=2)
	size_value_w = models.DecimalField(max_digits=9, decimal_places=2)
	size_label = models.CharField(choices=SIZE_LABEL,max_length=500, null=True,blank=True)
	size_value = models.DecimalField(max_digits=9, decimal_places=2)

class ProductSizeSet(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)
	sizes = models.ManyToManyField(ProductSize)

class ProductAttribute(models.Model):
	attribute = models.CharField(max_length=1000)

class ProductAttributes(models.Model):
	attributes = models.ManyToManyField(ProductAttribute)	

class ProductAttributesSets(models.Model):
	attributes_set_name = models.CharField(max_length=1000)
	attributes_set = models.ForeignKey(ProductAttributes, on_delete=models.CASCADE)

class ProductSpecification(models.Model):
	specification_name 	= models.CharField(max_length=1000, null=True,blank=True)
	specification_value = models.CharField(max_length=1000, null=True,blank=True)
	specification_description = RichTextField(max_length=10000, null=True,blank=True)

class ProductSpecifications(models.Model):
	specifications = models.ManyToManyField(ProductSpecification)

class ProductSpecificationsSets(models.Model):
	specifications_set_name = models.CharField(max_length=1000)
	specifications_set 	= models.ForeignKey(ProductSpecifications, on_delete=models.CASCADE)

class ProductGalleryImage(models.Model):
	image_name = models.CharField(max_length=300)
	image = models.ImageField(upload_to='media/PRODUCT/GALLERY_IMAGES/', null=True, blank=True, max_length=500)	

class ProductGalleryImagesSet(models.Model):
	images = models.ManyToManyField(ProductGalleryImage) 	

class ProductImageGallery(models.Model):
	gallery_name = models.CharField(max_length=300)
	images = models.ForeignKey(ProductGalleryImagesSet, on_delete=models.CASCADE)

class Category(MPTTModel):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)
	description = models.TextField(max_length=50, null=True,blank=True)
	category_icon = models.ImageField(upload_to='media/PRODUCT/CATEGORY/CATEGORY_ICONS/', null=True, blank=True, max_length=500)
	category_cover_image = models.ImageField(upload_to='media/PRODUCT/CATEGORY/CATEGORY_COVER_IMAGES/', null=True, blank=True, max_length=500)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

	def __str__(self):
		return self.title

	class MPTTMeta:
		ordering = ('title',)
		order_insertion_by = ['title']
		level_attr = 'mptt_level'

	def get_absolute_url(self):
		return reverse('ecommerce:category', args=[self.slug])

class ProductDetailsListItem(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)	

	details_description = RichTextField(max_length=10050, null=True,blank=True)

	def __str__(self):
		return self.title

class ProductDetailsListItems(models.Model):
	product_details_list_items = models.ManyToManyField(ProductDetailsListItem)	

class ProductDetailsList(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)

	product_details_list_items = models.ForeignKey(ProductDetailsListItems, on_delete=models.CASCADE, null=True,blank=True)	
	
	def __str__(self):
		return self.title

class ProductKeywords(models.Model):
	keyword = models.CharField(max_length=300)

	def __str__(self):
		return str(self.keyword)

class ProductKeywordsSet(models.Model):
	keywords = models.ManyToManyField(ProductKeywords)

	def __str__(self):
		return str(self.keywords)

class ProductMetas(models.Model):
	product_meta_title 	= models.CharField(max_length=60)
	product_meta_description = models.TextField(max_length=160)
	product_meta_keywords 	= models.ForeignKey(ProductKeywordsSet, on_delete=models.CASCADE ,max_length=300)

	product = models.ForeignKey('Product', on_delete=models.CASCADE,null=True, blank=True)

	author = models.ManyToManyField(settings.AUTH_USER_MODEL,null=True, blank=True)



	def __str__(self):
		return str(self.product_meta_title)

class ProductTagsCloud(models.Model):
	tag_cloud = models.CharField(max_length=300,null=True, blank=True) 

class ProductTagsClouds(models.Model):
	tag_clouds = models.ManyToManyField(ProductTagsCloud, null=True, blank=True)

class ProductTagsCloudsSet(models.Model):
	tag_clouds_set = models.ForeignKey(ProductTagsClouds, on_delete=models.CASCADE,null=True, blank=True)

class BrandSocialFollowURL(models.Model):
	brand_social_profile_name		= models.CharField(max_length=300, null=True, blank=True)
	brand_social_profile_URL		= models.URLField(null=True, blank=True)

class BrandSocialFollowURLS(models.Model):
	social_profiles_URLS 		= models.ManyToManyField(BrandSocialFollowURL,  blank=True)

	def __str__(self):
		return str(self.social_profiles_URLS) 

class BrandSocialFollows(models.Model):
	brand_social_follows_name	= models.CharField(max_length=300, null=True, blank=True)
	social_profiles_URLS 		= models.ForeignKey(BrandSocialFollowURLS, on_delete=models.CASCADE, blank=True)

	def __str__(self):
		return str(self.social_profiles_URLS) 

class BrandProduct(models.Model):
	products 		= models.ForeignKey('ecommerce.Product',  on_delete=models.CASCADE, related_name='brand_product',  blank=True)

	def __str__(self):
		return str(self.social_profiles_URLS) 

class BrandProducts(models.Model):
	products 		= models.ManyToManyField('ecommerce.Product',  related_name='brand_product_set',  blank=True)

	def __str__(self):
		return str(self.social_profiles_URLS) 

class Brand(models.Model):
	title = models.CharField(max_length=1000)
	slug = models.SlugField(max_length=1000)
	tagline = models.CharField(max_length=1000)
	websiteURL = models.URLField(max_length=300, null=True, blank=True)
	phone_number = models.CharField(max_length=300, null=True, blank=True)
	email_address = models.EmailField(max_length=300, null=True, blank=True)
	brand_logo	= models.ImageField(upload_to='media/PRODUCT/BRAND_LOGOS/', null=True, blank=True)
	brand_cover	= models.ImageField(upload_to='media/PRODUCT/BRAND_COVERS/', null=True, blank=True)
	description = RichTextField(null=True, blank=True)
	brand_social_follow	= models.ForeignKey(BrandSocialFollows, on_delete=models.CASCADE, null=True, blank=True)
	brand_products = models.ManyToManyField(BrandProducts, related_name='brand_products', null=True, blank=True)
	brand_followers	= models.ManyToManyField(CustomUser)

	def get_absolute_url(self):
		return reverse('ecommerce:brand', args=[self.slug])

	def __str__(self):
		return str(self.title) 

class ProductVariationImage(models.Model):
	product_image = models.ImageField(upload_to='media/PRODUCTS/FEATURED_IMAGES/')

	def __str__(self):
		return str(self.product_image)

class ProductVariableProductImageGallery(models.Model):
	product = models.CharField(max_length=300)
	images = models.ManyToManyField(ProductVariationImage)

	def __str__(self):
		return self.product


class ProductVariationType(models.Model):
	varitaion_type= models.CharField(max_length=1000)
	def __str__(self):

		return self.varitaion_type

class VariableColor(models.Model):
	title = models.CharField(max_length=300)
	slug = models.SlugField(max_length=300)
	color = ColorField(default='#FF0000')


	def get_absolute_url(self):
		return reverse('ecommerce:color', args=[self.slug])




class ProductVariable(models.Model):

	title = models.CharField(max_length=300)
	slug = models.SlugField(max_length=300)
	
	featured_image = models.ImageField(upload_to='media/PRODUCTS/VARIATIONS/VARIABLE_IMAGES/', blank=True, null=True)
	
	product_variable_image_gallery = models.ForeignKey(ProductVariableProductImageGallery, on_delete=models.CASCADE,null=True, blank=True)
	
	price_regular = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	price_sale = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	price_final = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	
	MSRP_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	MAP_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
	
	product_UPC = models.CharField(max_length=300, blank=True, null=True)
	product_SKU = models.CharField(max_length=300, blank=True, null=True)
	product_MODEL_ID = models.CharField(max_length=300, blank=True, null=True)
	
	product_is_featured = models.BooleanField(default=False)
	product_is_bestseller = models.BooleanField(default=False)
	product_is_on_sale 	= models.BooleanField(default=False)
	high_sell_through = models.BooleanField(default=False)
	
	description_short = RichTextField(null=True, blank=True)
	description_full = RichTextField(null=True, blank=True)
	
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField()
	
	size = models.ManyToManyField(ProductSizeSet)
	color = ColorField(default='#FF0000')

	WEIGHT_UNITS = (
			('kg','KG'),
			('lb','LB'),
			('oz','OZ'),
			('gm','Grams'),
			('mg','Milligrams'),
			('lt','Liters'),
			('cp','Cups'),

		)
	
	SIZE_LBLS = (('qt','QT'),)

	product_size_vlu =  models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
	product_size_lbl =  models.CharField(choices=SIZE_LBLS, max_length=100, null=True, blank=True)	
	product_weights_lbl = models.CharField(choices=WEIGHT_UNITS, max_length=1000, null=True, blank=True)
	item_weight_value = models.CharField( max_length=1000, null=True, blank=True)
	MEASUREMENTS_UNITS = (
			('in','Inches'),
			('cm','cm'), )
	product_measurements_H = models.CharField(max_length=500,null=True,blank=True)
	product_measurements_L = models.CharField(max_length=500,null=True,blank=True)
	product_measurements_W = models.CharField(max_length=500,null=True,blank=True)
	product_measurements_lbl = models.CharField(choices=MEASUREMENTS_UNITS, max_length=1000, null=True, blank=True)

	def __str__(self):
		return self.title

class ProductVariations(models.Model):
	type_of_variation = models.ManyToManyField(ProductVariationType, max_length=200)
	variations_id = models.CharField(max_length=300)
	variations_name = models.CharField(max_length=300)
	variations = models.ManyToManyField(ProductVariable, blank=True, null=True)

	def __str__(self):
		return self.variations_name

		

class ProductColor(models.Model):
	title = models.CharField(max_length=300)
	slug = models.SlugField(max_length=300)

	color = ColorField(default='#FF0000')

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('ecommerce:color', args=[self.slug])


class ProductStockManagement(models.Model):

	product_name = models.CharField(max_length=400)

	STOCK_STATUS_OPTIONS = (
			('in_stock','In stock'),
			('out_of_stock','Out of stock'),
		
		)
	stock_status = models.CharField(max_length=300,choices=STOCK_STATUS_OPTIONS)

	stock_quantity = models.IntegerField(blank=True,null=True)

	alert_low_stock	= models.BooleanField(max_length=1000, default=False, null=True, blank=True)

	low_quantity_to_alert= models.IntegerField(null=True, blank=True, help_text="Enter the minimum amount of stock to begin alert")


class Product(models.Model):
	product_metas_set = models.ForeignKey(ProductMetas, on_delete=models.CASCADE, related_name='product_metas',null=True, blank=True)
	

	product_meta_title 	= models.CharField(max_length=60, null=True,blank=True)
	product_meta_description = models.TextField(max_length=160, null=True,blank=True)
	product_meta_keywords 	= models.ForeignKey(ProductKeywordsSet, on_delete=models.CASCADE ,max_length=300, null=True,blank=True)

	
	PRODUCT_TYPE = (
						('single_product','Single product'),
						('variable_product','Variable product'),
						('groupped_product','Groupped product'),
					)
	product_type = models.CharField(max_length=1000, choices=PRODUCT_TYPE)

	PRODUCT_STATUS = (
						('is_inactive','Inactive'),
						('is_active','Active'),
						('published','Published'),
					)

	product_status = models.CharField(choices=PRODUCT_STATUS, max_length=100,null=True, blank=True)

	title = models.CharField(max_length=250, null=True,blank=True)
	slug = models.SlugField(max_length=250, null=True,blank=True)

	featured_image = models.ImageField(default='media/ECOMMERCE/PRODUCTS/FEATURED_IMAGES/default.png', upload_to='media/ECOMMERCE/PRODUCTS/FEATURED_IMAGES/', null=True, blank=True)
	image_galley= models.ForeignKey(ProductImageGallery, on_delete=models.CASCADE, related_name='product_image_gallery',null=True, blank=True)
	
	price_regular = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
	price_sale = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True, )
	price_MSRP  = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)


	TAX_RATE = {}

	tax_rate_ko = models.CharField(max_length=50, choices=TAX_RATE, null=True, blank=True)
	tax_rate = models.ForeignKey(TaxSettings, on_delete=models.CASCADE, null=True,blank=True)

	brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand',null=True, blank=True)

	category = models.ManyToManyField(Category, null=True,blank=True)

	description_short = RichTextField(max_length=2000, null=True,blank=True)
	description_full = RichTextField(max_length=50000, null=True,blank=True)

	product_details_list = models.ForeignKey(ProductDetailsList, on_delete=models.CASCADE, null=True, blank=True)
	product_attributes_set = models.ForeignKey(ProductAttributesSets, on_delete=models.CASCADE, related_name='product_attributes_set',null=True, blank=True)
	product_specifications_set = models.ForeignKey(ProductSpecificationsSets, on_delete=models.CASCADE, related_name='product_specifications_set',null=True, blank=True)
	
	date_added = models.DateTimeField(auto_now_add=True)

	product_SKU = models.CharField(max_length=50, null=True,blank=True)
	product_UPC = models.CharField(max_length=50, null=True,blank=True)
	product_STYLE = models.CharField(max_length=50, null=True,blank=True)

	product_is_featured = models.BooleanField(default=False)
	product_is_bestseller = models.BooleanField(default=False)
	product_is_on_sale 	= models.BooleanField(default=False)

	high_sell_through = models.BooleanField(default=False)
	tag_clouds = models.ForeignKey(ProductTagsCloudsSet, on_delete=models.CASCADE,null=True, blank=True)

	likes = models.ManyToManyField(CustomUser,null=True, blank=True, related_name='product_likes')


	product_stock_management = models.ForeignKey(ProductStockManagement, on_delete=models.CASCADE, related_name='product_stock_management',null=True, blank=True)


	WEIGHT_UNITS = (
			('kg','KG'),
			('lb','LB'),
			('oz','OZ'),
			('gm','Grams'),
			('mg','Milligrams'),
		)
	
	product_weights_lbl = models.CharField(choices=WEIGHT_UNITS, max_length=1000, null=True, blank=True)
	item_weight_value = models.IntegerField(null=True,blank=True)

	MEASUREMENTS_UNITS = (
			('in','Inches'),
		)

	product_measurements_H = models.IntegerField(null=True,blank=True)
	product_measurements_L = models.IntegerField(null=True,blank=True)
	product_measurements_W = models.IntegerField(null=True,blank=True)
	product_measurements_lbl = models.CharField(choices=MEASUREMENTS_UNITS, max_length=1000, null=True, blank=True)
	product_size = models.ManyToManyField(ProductSizeSet, null=True, blank=True)
	color = ColorField(default='#FF0000')
	product_color = models.ManyToManyField(ProductColor,null=True, blank=True)


	product_variations_set = models.ForeignKey(ProductVariations, on_delete=models.CASCADE, null=True, blank=True)


	product_reviews_rating = models.ManyToManyField('Reviews', null=True, blank=True)

	product_saves = models.ManyToManyField(CustomUser, null=True, blank=True)

	def get_absolute_url(self):
		return reverse('ecommerce:product', args=[self.slug])

	def __str__(self):
		return str(self.title)

class Payment(models.Model):

	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)

	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	
	CARD_TYPE = (
			('visa','VISA'),
			('mastercard','MasterCard'),
			('american_express','American Express'),
			('discover','Discover'),
		)
	
	PAYMENT_METHOD = (
		('bank_account','Bank account'),
		('credit_or_debit_card','Credit or debit card'),
		('paypal','PayPal'),
	)

	payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=20)

	card_number = models.CharField(max_length=50)
	expiration_date = models.CharField(max_length=50)
	security_code = models.CharField(max_length=50)
	zip_code = models.CharField(max_length=50)

	card_type = models.CharField(choices=CARD_TYPE, max_length=1000, null=True, blank=True)

	set_to_default = models.BooleanField(default=False, null=True, blank=True)

	def __str__(self):
		return  f"{self.user}'s payment | {self.card_number}"

class Address(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)

	phone_number = models.CharField(max_length=300, null=True, blank=True)
	address_id_name = models.CharField(max_length=1000)

	TYPE_OF_ADDRESS = (
				('billing_address','Billing address'),
				('shipping_address','Shipping address'),
				('p_o_box_number','Post office box number'),
			)

	type_of_address	=	models.CharField(max_length=1000, choices=TYPE_OF_ADDRESS)

	#order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, related_name='order_address',null=True,blank=True)
	
	street_name_01	=	models.CharField(max_length=1000, null=True, blank=True)
	street_name_02	=	models.CharField(max_length=1000, null=True, blank=True)
	street_city		=	models.CharField(max_length=1000, null=True, blank=True)
	street_state	=  USStateField()
	street_zip_code	=	USZipCodeField()

	default_address = models.BooleanField(default=False,null=True, blank=True)

	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address_id_name



class OrderVarItem(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)

	var_product = models.ForeignKey(ProductVariable,on_delete=models.CASCADE,null=True,blank=True)
	
	quantity = models.IntegerField(default=1)

	TAX_RATE = {}

	tax_rate_ko = models.CharField(max_length=50, choices=TAX_RATE, null=True, blank=True)
	tax_rate = models.ForeignKey(TaxSettings, on_delete=models.CASCADE, null=True,blank=True)

	
	def get_item_total(self):
		if self.product.price_sale:
			price_sale = self.product.price_sale
			if price_sale:
				item_total = self.product.price_sale * self.quantity
		else:
				item_total = self.product.price_regular * self.quantity 
		return item_total

	def __str__(self):
		return str(self.user)

	def get_total_item_weight(self):
		USPS_First_Class_Rate_test = 6
		item_quantity = self.quantity
		koyo = USPS_First_Class_Rate_test * item_quantity

		return koyo

class OrderItem(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
	product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
	var_product = models.ForeignKey(ProductVariable,on_delete=models.CASCADE,null=True,blank=True)
	quantity = models.IntegerField(default=1)

	TAX_RATE = {}

	tax_rate_ko = models.CharField(max_length=50, choices=TAX_RATE, null=True, blank=True)
	tax_rate = models.ForeignKey(TaxSettings, on_delete=models.CASCADE, null=True,blank=True)

	def __str__(self):
		return str(self.user)

	def get_total_item_weight(self):
		total_item_weight = self.product.item_weight_value * self.quantity
		total_weight_per_item = 2
		total_weight = total_item_weight * total_weight_per_item

		return total_item_weight

	def get_total_item_cost(self):
		items_prices_to_add=[]
		if self.product.price_sale:
			price_sale = self.product.price_sale

			if price_sale:
				item_total = self.product.price_sale * self.quantity
		else:
				item_total = self.product.price_regular * self.quantity 


		return item_total



class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)

	ORDER_STATUS = (
			('pending','Pending'),
			('processing','Processing'),
			('active','Active'),
			('unshipped','Unshipped'),
			('shipped','Shipped'),
			('canceled','Canceled'),
		)

	order_status = models.CharField(max_length=30, choices=ORDER_STATUS, null=True,blank=True)
	

	order_items = models.ManyToManyField(OrderItem, null=True,blank=True)
	
	var_order_items = models.ManyToManyField(OrderItem, null=True,blank=True, related_name='var_order_items')
	
	address_billing = models.ForeignKey(Address, on_delete=models.CASCADE, null=True,blank=True, related_name='order_billing_address')
	address_shipping = models.ForeignKey(Address, on_delete=models.CASCADE, null=True,blank=True, related_name='order_shipping_address')
	
	payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True,blank=True)
	
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	date_canceled = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	date_shipped = models.DateTimeField(null=True, blank=True)
	
	shipping_rate = models.ForeignKey('ShippingSettings', on_delete=models.CASCADE, null=True,blank=True)
	
	tax_rate = models.ForeignKey(TaxSettings, on_delete=models.CASCADE, null=True,blank=True)

	refund_requested = models.BooleanField(default=False, null=True,blank=True)
	refund_requested_accepted = models.BooleanField(default=False, null=True,blank=True)
	refund_requested_proccessed = models.BooleanField(default=False, null=True,blank=True)

	def __str__(self):
		return str(self.user)

	def get_sub_total(self):

		pass

	def get_shipping_rate(self):
		
		pass
	

	def get_tax_rate(self):
		pass


	def get_grand_total(self):

		return None


	def get_coupon_deduction(self):
		deducted_price =  self.get_grand_total()

class Refunds(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True,blank=True, related_name='refund_for_user_ecommerce')
	order = models.ForeignKey(Order,on_delete=models.CASCADE, null=True,blank=True)

	reason_for_refund = models.TextField(max_length=300,null=True,blank=True )

	refund_accepted = models.BooleanField(default=False)

class ShippingCarrier(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)

	shipping_carrier_logo = models.ImageField(upload_to='media/SHIPPING_CARRIERS_LOGOS', null=True,blank=True)
	description = RichTextField(max_length=500, null=True,blank=True)

	def __str__(self):
		return str(self.title)	



class ShippingSettings(models.Model):
	SHIPPING_TYPE= {
		('free_shipping','Free Shipping'),
		('free_express_shipping','Free Express Shipping'),
		('free_2_day_shipping','Free 2 Day Shipping'),
	}
	shipping_type = models.CharField(max_length=70, choices=SHIPPING_TYPE, null=True, blank=True)

	SHIPPING_STATUS = {
		('unshipped','Unshipped'),
		('preshipment','Pre-shipment'),
		('shipped','Shipped'),
		('delivered','Delivered'),
	}
	shipping_status = models.CharField(max_length=50, choices=SHIPPING_STATUS, null=True, blank=True)
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)

	carrier = models.ForeignKey(ShippingCarrier, on_delete=models.CASCADE, null=True,blank=True )

	shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
	shipping_cost_TAX = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)

	tracking_number = models.CharField(max_length=50, null=True,blank=True)
	tracking_number_URL = models.URLField(max_length=50, null=True,blank=True)

	date_shipped = models.DateTimeField()
	date_estimated_delivery = models.DateTimeField()

	note = RichTextField(max_length=500, null=True,blank=True)

	def __str__(self):
		return str(self.title)


	def get_shipping_total(self):

		shipping_total_cost = self.shipping_cost + self.shipping_cost_TAX

		return shipping_total_cost






class Coupon(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)

	description = models.TextField(max_length=50, null=True,blank=True)

	def __str__(self):
		return self.title


class Newsletters(models.Model):
	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)

	first_name = models.CharField(max_length=50, null=True,blank=True)
	last_name = models.CharField(max_length=50, null=True,blank=True)

	phone_number = models.CharField(max_length=50, null=True,blank=True)

	email_address = models.EmailField(max_length=30, null=True, blank=True)

	def __str__(self):
		return self.email_address


class Reviews(models.Model):

	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True,blank=True)
	user_IP = models.CharField(max_length=50, null=True,blank=True)

	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)


	RATINGS = {
		('1','1'),
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),
	}

	rating = models.CharField(max_length=50,choices=RATINGS, null=True,blank=True)


	review_comment = RichTextField(max_length=300)

	date_posted = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField()

	STATUS = {
		('draft','Draft'),
		('published','Published'),

	}

	status = models.CharField(max_length=50, choices=STATUS, null=True, blank=True)



	def __str__(self):
		return self.user.username



class Wishlist(models.Model):

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

	title = models.CharField(max_length=50, null=True,blank=True)
	slug = models.SlugField(max_length=50, null=True,blank=True)

	wishlist_cover_image = models.ImageField(upload_to='media/WISHLIST_COVER_IMAGES/', null=True,blank=True)

	description = RichTextField(max_length=500, null=True,blank=True)

	products = models.ManyToManyField(Product, null=True,blank=True)

	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now_add=False ,null=True,blank=True)


	def get_absolute_url(self):
		return reverse('ecommerce:wishlist', args=[self.slug])


	def __str__(self):
		return self.title










