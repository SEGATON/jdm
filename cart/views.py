from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.http import JsonResponse
from django.http import HttpResponseRedirect

from .cart import Cart

from django.contrib import messages

from ecommerce.models import Product



# Create your views here.


def front_page(request):

	cart = Cart(request)
	cart_products = cart.get_current_cart_product

	cart = Cart
	cart.add_product

	return render(request, 'cart/front_page.html',{

			'cart': cart,
			'cart_products':cart_products

		})

