from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import admin

from .models import Category
from .models import Product
from .models import Brand
# Register your models here.
from .models import Order
from .models import OrderItem
from django.template import RequestContext

from .filters import ProductFilter, ProductRegularPriceFilter
from django.template.loader import render_to_string, get_template

from .forms import EditOrder
from .forms import AddPaymentMethod
from .forms import AddAddressForm
from .forms import EditPaymentMethod
from .forms import EditAddressForm
from .forms import NewslettersSubscriptionForm
from .forms import CreateWishlistForm

from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.contrib import messages
from django.db.models import Q

from .models import Address
from .models import Payment
from .forms import AddToWishlistForm
from .models import Wishlist

from .models import ProductMetas
from .models import ProductVariable

from django.views import generic
from bootstrap_modal_forms.generic import BSModalCreateView












def front_page(request):
	products = Product.objects.all()


	return render(request, 'ecommerce/front_page.html', {
			'products':products,

		})

def products(request):

	products = Product.objects.all()

	f = ProductFilter(request.GET, queryset=Product.objects.all())
	tf = ProductFilter(request.GET, queryset=Product.objects.all())


		
	return render(request, 'catalog/products.html', {
			'products':products,
			'f':f,
			'tf':tf,
	
	
		})




def brands(request):
	brands = Brand.objects.all()
	return render(request, 'catalog/brands/brand.html', {

			'brands':brands

		})

def brand(request, slug):
	brand = get_object_or_404(Brand, slug=slug)
	return render(request, 'catalog/brands/brand.html', {

			'brand':brand

		})




class Products(generic.ListView):
	template_name = 'catalog/products.html'
	model = Product
	context_object_name = 'products'



def product(request, slug):

	product = get_object_or_404(Product, slug=slug)

	for cat in product.category.all():
		category = cat 

	related_products = Product.objects.filter(category=category).exclude()

	latest_products = Product.objects.filter(category=category)


	liked = False

	if product.likes.filter(id=request.user.id).exists():
		liked = True

	return render(request, 'catalog/product.html', {
			'product':product,
			'latest_products':latest_products,
			'related_products':related_products,
			'liked':liked,

		})


def menu(request):
	
	return {
		'menu':Category.objects.all()
	}

def ecommerce_categories(request):

	return {
		'ecommerce_categories':Category.objects.all()
	}

def ecommerce_categories_widget(request):

	return {
		'ecommerce_categories_widget':Category.objects.all()[:6]
	}

def category(request, slug):

	category = get_object_or_404(Category, slug=slug)
	products = Product.objects.filter(category=category)
	f = ProductFilter(request.GET, queryset=Product.objects.filter(category=category))



	return render(request, 'catalog/categories/category.html', {
			'category':category,
			'products':products,
			'f':f,
			'title':'hello'
		})


def all_categories(request):
	all_categories = Category.objects.all()
	return render(request, 'catalog/categories/all_categories.html', {
			'all_categories':all_categories
		})
def orders(request):
	orders = Order.objects.filter(user=request.user)
	return render(request, 'orders/orders.html', {
			'orders':orders
		})	

def order(request, pk):
	order = get_object_or_404(Order, pk=pk)
	return render(request, 'orders/order.html', {
			'order':order
		})	

def edit_order(request, pk):
	order = get_object_or_404(Order, pk=pk)
	if request.method ==  'POST':
		edit_order_form = EditOrder(request.POST, instance=order)
		if edit_order_form.is_valid():
			tarakan = edit_order_form.save(commit=False)
			tarakan.instance = request.user
			tarakan.save()
			return redirect('ecommerce:order', pk=pk)
	else:
		edit_order_form = EditOrder()
	return render(request, 'orders/manage_orders/edit_order.html', {
			'order':order,
			'edit_order_form':edit_order_form
		})

def checkout(request, pk):
	order = get_object_or_404(Order, pk=pk)

	itemm = None
	for item in order.order_items.all():
		itemm = item

	paypal_dict = {
		'business':settings.PAYPAL_RECIEVER_EMAIL,
		'item_name':itemm,
		'amount':order.get_grand_total(),
		'invoice':order.id,
		'notify_url': request.build_absolute_uri(reverse('paypal-ipn')),
		'returns': request.build_absolute_uri(reverse('ecommerce:returns')),
		'cancel_order':request.build_absolute_uri(reverse('ecommerce:cancel_order', args=[pk])),
		'refunds':request.build_absolute_uri(reverse('ecommerce:refunds')),

	}

	form = PayPalPaymentsForm(initial=paypal_dict)

	context = {
		'form':form,
		'order':order,

		}

	return render(request, 'checkout/checkout.html', context)	

class CustomPayPalPaymentsForm(PayPalPaymentsForm):

    def get_html_submit_element(self):
        return """<button type="submit">Continue on PayPal website</button>"""

	

@login_required
def process_payment(request, pk):
	order = Order.objects.filter(user=request.user)

	return render(request, 'payments/process_payment.html', {})	


def returns(request):
	return render(request, 'orders/returns.html', {

		})

def refunds(request):
	return render(request, 'orders/refunds.html', {

		})

def cancel_order(request, pk):
	return render(request, 'orders/cancel_order.html', {
		
		})






def add_single_product_to_cart(request):
	# get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		product = get_object_or_404(Product, id=product_id)

		cart.add(product=product, quantity=product_qty)

		cart_quantity = cart.__len__()


		response = JsonResponse({'Product': product.title})

		messages.success(request, ("Product Added To cart!"))

		return response




@login_required
def add_single_product_to_cart(request, pk):
	
	product = get_object_or_404(Product, pk=pk)# are you sure its Product and not OrderItem model you pass to get_object_or...?? Think about it!!!
	order_item, created = OrderItem.objects.get_or_create(product=product, user=request.user)
	order_po = Order.objects.filter(user=request.user)

	if order_po.exists():
		order = order_po[0]
		if order.order_items.filter(product__pk=product.pk).exists():
			order_item.quantity += 1
			order_item.save()
			messages.success(request, "Product" + ' ' + str(product)   + ' ' + 'was added to your cart.')

			return HttpResponseRedirect(request.META['HTTP_REFERER'])
			
		else:

			order.order_items.add(order_item)

	return HttpResponseRedirect(request.META['HTTP_REFERER'])



@login_required
def decrement_cart_item_quantity(request, pk):
	product = get_object_or_404(Product, pk=pk) 
	order_po = Order.objects.filter(user=request.user)

	if order_po.exists():
		order = order_po[0]
		if order.order_items.filter(product__pk=product.pk).exists():
			order_item = OrderItem.objects.filter(product=product, user=request.user)[0]

			if order_item.quantity > 1:
				order_item.quantity -= 1
				order_item.save()
			else:
				order.order_items.remove(order_item)
			messages.info(request, "wait not now")
			return redirect('ecommerce:order')
		else:
			messages.info(request, "dfddfdfd")
			return redirect('ecommerce:product', pk=pk)
	else:
		messages.info(request, "ddfdfdfdfdfdfdf")
		return redirect('ecommerce:product', pk=pk)



@login_required
def add_variation_product_to_cart(request, pk):

	
	return HttpResponseRedirect(request.META['HTTP_REFERER'])




def cart(request):
	order = Order.objects.get(user=request.user)
	return render(request,'cart/cart.html', {
			'order':order
		})


def cart_summary(request):

	cart = Cart(request)

	cart_products = cart.get_prods

	return render(request, 'cart/cart_je_version.html' , {
			'cart_products ':cart_products 
		})



def remove_order_item_from_cart(request, pk):
	koko= OrderItem.objects.filter(pk=pk)
	koko.delete()
	
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def process_coupon(request, pk):

	if request.method == 'POST':
		coupon_code = request.POST['coupon_code_tf']
		messages.success(request, "Coupon coode added successfully!")

	#return HttpResponseRedirect(request.META['HTTP_REFERER'])
	return render(request, 'cart/cart.html', {
			'coupon_code':coupon_code
		})	
def increment_cart_item_quantity(request, pk):

	order_item = get_object_or_404(OrderItem, pk=pk)
	order_item +=1
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

def decrement_cart_item_quantity(request, pk):
	order_item_quantity_to_decrease = get_object_or_404(OrderItem, pk=pk)
	order = Order.objects.filter(user=request.user)
	product = get_object_or_404(Product, pk=pk)
	order_item = OrderItem.objects.get(product=product)

	return HttpResponseRedirect(request.META['HTTP_REFERER'])



def addresses(request):
	addresses = Address.objects.filter(user=request.user)

	return render(request, 'orders/manage_orders/order_details/addresses/addresses.html', {
			'addresses':addresses
		})

@login_required
def add_address(request):
	if request.method == 'POST':
		add_address_form = AddAddressForm(request.POST)
		if add_address_form.is_valid():
			potaga = add_address_form.save(commit=False)
			potaga.user = request.user 
			potaga.save()
			messages.success(request, "Address added")
			return redirect('ecommerce:addresses')
	else:
		add_address_form = AddAddressForm()
	return render(request, 'orders/manage_orders/order_details/addresses/add_address.html', {
			'add_address_form':add_address_form
		})

@login_required
def edit_address(request, pk):
	edit_address_form = EditAddressForm()
	return render(request, 'orders/manage_orders/order_details/addresses/edit_address.html', {
			'edit_address_form':edit_address_form
		})

@login_required
def delete_address(request, pk):
	address = get_object_or_404(Address, pk=pk)
	address.delete()
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

def payments(request):
	payments = Payment.objects.filter(user=request.user)
	return render(request, 'orders/manage_orders/order_details/payments/payments.html', {
				'payments':payments
		})

@login_required
def add_payment(request):
	if request.method == 'POST':
		add_payment_method_form = AddPaymentMethod(request.POST)
		if add_payment_method_form.is_valid():
			koko = add_payment_method_form.save(commit=None)
			koko.user = request.user 
			koko.save()
			return redirect('ecommerce:payments')
	else:
		add_payment_method_form = AddPaymentMethod()
	return render(request, 'orders/manage_orders/order_details/payments/add_payment.html', {
			'add_payment_method_form':add_payment_method_form
		})


@login_required
def delete_payment_method(request, pk):
	payment = get_object_or_404(Payment, pk=pk)
	payment.delete()

	return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def edit_payment_method(request, pk):
	payment = get_object_or_404(Payment, pk=pk)

	edit_payment_method = EditPaymentMethod()

	return render(request, 'orders/manage_orders/order_details/payments/edit_payment.html', {

		})

def search(request):
	search_query = request.GET.get("search_ecommerce_app_tf")
	
	search_querySet = Product.objects.filter(Q(title__icontains=search_query))

	return render(request, 'components/search_results.html', {
				'search_querySet':search_querySet,

		})

def testing(request):

	return render(request, 'ecommerce/testing.html', {

		})

def newsletters_subscription_form(request):
	if request.method =='POST':
		newsletters_subscription_form = NewslettersSubscriptionForm(request.POST)
		if newsletters_subscription_form.is_valid():
			newsletters_subscription_form.save()
			messages.info(request, 'You have subscribed successfully.')

	else:
		newsletters_subscription_form = NewslettersSubscriptionForm()


	return {
		'newsletters_subscription_form':newsletters_subscription_form
	}


def quick_view(request,  slug):

	product = get_object_or_404(Product, slug=slug)
	context = {
		'product':product
	}

	return JsonResponse(product)




@login_required
def like_product(request, pk):

	product = get_object_or_404(Product, pk=pk)

	liked = False

	if product.likes.filter(id=request.user.id).exists():
		product.likes.remove(request.user)
		liked = False
	else:
		product.likes.add(request.user)
		liked = True


	return HttpResponseRedirect(request.META['HTTP_REFERER'])




@login_required
def unlike_product(request, pk):

	product = get_object_or_404(Product, pk=pk)

	return HttpResponseRedirect(request.META['HTTP_REFERER'])


# -------------------------------WISH-LIST SYSYEM STARTS----------------------------------#

@login_required
def wishlists(request):
	wishlists = Wishlist.objects.filter(user=request.user)
	return render(request, 'catalog/wishlist/wishlists.html', {
			'wishlists':wishlists

		})



@login_required
def wishlist(request, pk):

	wishlist = get_object_or_404(Wishlist, pk=pk)

	return render(request, 'catalog/wishlist/wishlist.html', {
			'wishlist':wishlist

		})



@login_required
def add_item_from_wishlist(request, pk):

	messages.success(request, "Item added to wishlist")

	return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def remove_item_from_wishlist(request, pk):


	return HttpResponseRedirect(request.META['HTTP_REFERER'])




@login_required
def create_wishlist(request):

	create_wishlist_form = CreateWishlistForm()

	return render(request, 'catalog/wishlist/create_wishlist.html', {
	
			'create_wishlist_form':create_wishlist_form
		})
	
@login_required
def delete_wishlist(request, pk):
	pass


def add_to_wishlist_form(request):

	context = {
		'form':  AddToWishlistForm()
		}

	return context


# -------------------------------WISH-LIST SYSYEM ENDS ----------------------------------#





















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































