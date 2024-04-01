
from ecommerce.models import Product

from memberships.models import Profile


class Cart():

	def __init__(self, request):
		self.session = request.session
		self.request = request

		cart = self.session.get('session_key')

		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}

		self.cart = cart
	
	def display_greeting_message(self):

		greeting_message = "Hello World"

		return greeting_message

	#---------------------------------------

	def add_product(self, product, quantity):
		product_id = str(product)
		product_qty = str(quantity)

		if product_id in self.cart:
			pass
		else:
			self.cart[product_id] = int(product_qty)


		self.session.modified = True

		if self.request.user.is_authenticated:
			current_user = Profile.objects.filter(user__id=self.request.user.id)

			cartoto = str(self.cart)
			cartoto = cartoto.replace("\'", "\"")

			current_user.update(old_cart=str(cartoto))

	def update_product(self):
		pass

	def delete_product(self):
		pass

	#---------------------------------------

	def __len__(self):
		return len(self.cart) 

	#---------------------------------------

	def get_current_cart_product(self):

		product_ids = self.cart.keys()
		

		# i changed this to slug, becuae the view takes a slug instead of id
		# hence slug__in instead of id__in, take a look and see how to improve

		products = Product.objects.filter(slug__in=product_ids)

		return products

	#---------------------------------------

	def get_cart_subtotal(self):
		pass 

	def get_shipping_rates(self):
		pass 

	def get_dropship_rate(self):
		pass 

	def get_tax_settings(self):
		pass

	def get_coupon_settings(self):
		pass

	def get_grandtotal(self):
		pass

