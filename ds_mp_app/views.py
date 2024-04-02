from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Order,OrderItem
# Create your views here.
from ecommerce.models import Product, Category, Brand
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from .models import Refunds
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from paypal.standard.forms import PayPalPaymentsForm

def search_products(request):
	return {
		'search_products_form':SearchProductForm()
	}

def dashboard(request):

	products = Product.objects.all()

	return render(request, 'dashboard/dashboard.html', {

			'products':products

		})


def front_page(request):
	products = Product.objects.all()
	return render(request, 'ds_mp_app/front_page.html', {
			'products':products,
			'title': 'DSMP - Dropship marketplace | dropship thousands of products'
		})




def checkout(request):
	

    # What you want the button to do.
    paypal_dict = {
        "business": "receiver_email@example.com",
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        #"return": request.build_absolute_uri(reverse('your-return-view')),
        #"cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }
    order = Order.objects.get(user=request.user)
    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form,"order":order}
    return render(request, "checkout/checkout.html", context)





class CartView(LoginRequiredMixin, View):

	def get(self, *args, **kwargs):

		try:

			order = Order.objects.get(user=self.request.user)

			context = {

				'object':order
			}

			return render(self.request, 'orders/cart.html', context)

		except ObjectDoesNotExist:

			messages.warning(self.request, "No active order <!>")

			return redirect('/')












def about_us(request):
	return render(request, 'static_pages/about_us.html', {
			'title': 'DSMP | About us'
		
		})

def contact_us(request):
	return render(request, 'static_pages/contact_us.html', {
			'title': 'DSMP | Contact us'
		
		})

def privacy_policy(request):
	return render(request, 'static_pages/privacy_policy.html', {
			'title': 'DSMP | Privacy policy'
		
		})

def terms_conditions(request):
	return render(request, 'static_pages/terms_conditions.html', {
			'title': 'DSMP | Terms of Use'
		})

def do_not_sell_my_personal_information(request):
	return render(request, 'static_pages/do_not_sell_my_personal_information.html', {
			'title': 'DSMP | Do No Sell My Personal Infomation'
		})

def dropshipper_application(request):
	return render(request, 'static_pages/dropshipper_application.html', {
			'title': 'DSMP | Dropshipper application'
		})









def f_a_q(request):
	return render(request, 'static_pages/f_a_q.html', {
			'title': 'DSMP | F.A.Q'
		})

def policies(request):
	return render(request, 'static_pages/policies.html', {
			'title': 'DSMP | Policies'
		})

def private_labelleing(request):
	return render(request, 'static_pages/private_labelleing.html', {
			'title': 'DSMP | Private Labelleing'
		})

def for_businesses(request):
	return render(request, 'static_pages/for_businesses.html', {
			'title': 'DSMP | For businesses'
		})

def careers(request):
	return render(request, 'static_pages/careers.html', {
			'title': 'DSMP | Careers'
		})

def affiliation_program(request):

	return render(request, 'static_pages/affiliation_program.html', {
			'title': 'DSMP | Affiliation program'
		})

def help_center(request):

	return render(request, 'static_pages/help_center.html', {

			'title': 'DSMP | Help center'

		})













def categories(request):

	return {

		'categories':Category.objects.all()

	}


def category(request, slug):

	category = get_object_or_404(Category, slug=slug)

	return render(request, 'catalog/product.html', {

			'category':category

		})



def brands(request):

	brands = Brand.objects.all()

	return render(request, 'catalog/brands/brands.html', {

			'brands':brands

		})



def brand(request, slug):

	brand = get_object_or_404(Brand, slug=slug)

	products = brand.brand_products

	return render(request, 'catalog/brands/brand.html', {

			'brand':brand,
			'products':products

		})



def products(request):

	products = Product.objects.all()

	return render(request, 'catalog/products.html', {

			'products':products

		})

'''

def product(request, slug):

	product = get_object_or_404(Product, slug=slug)

	return render(request, 'catalog/product.html', {

			'product':product

		})
'''


def single_product(request, slug):

	product = get_object_or_404(Product, slug=slug)

	return render(request, 'catalog/single_product.html', {

			'product':product

		})

def variable_product(request, slug):



	return render(request, 'catalog/variable_product.html', {


		})






@login_required
def add_to_cart(request, slug):

	product = get_object_or_404(Product, slug=slug)
	#qty = request.POST['qty']
	order_item, created = OrderItem.objects.get_or_create(order_item=product,user=request.user)

	orderr = Order.objects.filter(user=request.user)
	if orderr.exists():
		order = orderr[0]

		if order.order_items.filter(order_item__slug=product.slug).exists():
			order_item.order_item_quantity += 1
			order_item.save()
			messages.info(request, "Updated successfully.")

			return HttpResponseRedirect(request.META['HTTP_REFERER'])
		else:
			order.order_items.add(order_item)
			messages.info(request, "Added successfully")

			return HttpResponseRedirect(request.META['HTTP_REFERER'])
	else:
		order_date = timezone.now()
		order = Order.objects.create(user=request.user, date_created=order_date)
		messages.info(request, "Addedd")
		messages.success(request, "button clicked")
	
		return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def dropship_variable_product(request, slug):

	messages.success(request, "button clicked")

	return HttpResponseRedirect(request.META['HTTP_REFERER'])







@login_required
def dropship_single_product(request, slug):

	product = get_object_or_404(Product, slug=slug)
	qty = request.POST['qty']
	order_item, created = OrderItem.objects.get_or_create(order_item=product,user=request.user)

	orderr = Order.objects.filter(user=request.user)
	if orderr.exists():
		order = orderr[0]

		if order.order_items.filter(order_item__slug=product.slug).exists():
			order_item.order_item_quantity += 1
			order_item.save()
			messages.info(request, "Updated successfully.")

			return HttpResponseRedirect(request.META['HTTP_REFERER'])
		else:
			order.order_items.add(order_item)
			messages.info(request, "Added successfully")

			return HttpResponseRedirect(request.META['HTTP_REFERER'])
	else:
		order_date = timezone.now()
		order = Order.objects.create(user=request.user, date_created=order_date)
		messages.info(request, "Addedd")
		messages.success(request, "button clicked")
	
		return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def dropship_variable_product(request, slug):

	messages.success(request, "button clicked")

	return HttpResponseRedirect(request.META['HTTP_REFERER'])







@login_required
def remove_item_from_cart(request, slug):

	product = get_object_or_404(Product, slug=slug)
	order_qs = Order.objects.filter(user=request.user)

	if order_qs.exists():

		order = order_qs[0]

		if order.order_items.filter(order_item__slug=product.slug).exists():

			order_item = OrderItem.objects.filter(order_item=product, user=request.user)[0]
			order.order_items.remove(order_item)
			order_item.delete()

			messages.info(request, "This item was removed from you cart.")

			return redirect('ds_mp_app:cart')
		else:
			messages.info(request, "This item is not in your cart.")
			return redirect('ds_mp_app:product', slug=slug)

	else:
		messages.info(request, "No active order.")

		return redirect('ds_mp_app:product', slug=slug)



@login_required
def remove_single_item_from_cart(request, slug):

	product = get_object_or_404(Product, slug=slug) 
	order_po = Order.objects.filter(user=request.user)

	if order_po.exists():
		order = order_po[0]
		if order.order_items.filter(order_item__slug=product.slug).exists():
			order_item = OrderItem.objects.filter(order_item=product, user=request.user)[0]

			if order_item.order_item_quantity > 1:
				order_item.order_item_quantity -= 1
				order_item.save()
			else:
				order.order_items.remove(order_item)
			messages.info(request, "wait not now")
			return redirect('ds_mp_app:cart')
		else:
			messages.info(request, "dfddfdfd")
			return redirect('ds_mp_app:product', slug=slug)
	else:
		messages.info(request, "ddfdfdfdfdfdfdf")
		return redirect('ds_mp_app:product', slug=slug)




@login_required
def orders(request):

	orders = Order.objects.filter(user=request.user)

	return render(request, 'orders/orders.html', {

			'orders':orders

		})


@login_required
def order(request, pk):

	order = get_object_or_404(Order, pk=pk)


	return render(request, 'orders/order.html', {

			'order':order,
		

		})



from .forms import RequestRefund


@login_required
def request_refund(request, pk):
	order = get_object_or_404(Order, pk=pk)
	if request.method == 'POST':
		request_refund_form = RequestRefund(request.POST)
		if request_refund_form.is_valid():
			cho = request_refund_form.save(commit=False)
			cho.user = request.user
			cho.order = order
			cho.save()

			return HttpResponseRedirect(request.META['HTTP_REFERER'])

	else:
		request_refund_form = RequestRefund()
	return render(request, 'returns_refunds/request_refund.html', {
			'request_refund_form':request_refund_form
		})




@login_required
def refund_requests(request):
	refund_requests = Refunds.objects.all()
	return render(request, 'returns_refunds/refund_requests.html', {
			'refund_requests':refund_requests
		})


@login_required
def refund_request(request, pk):
	refund_request = get_object_or_404(Refunds, pk=pk)
	return render(request, 'returns_refunds/refund_request.html', {
			'refund_request':refund_request
		})

