from django.urls import path
from . import views  

from .views import Products

app_name = 'ecommerce'

urlpatterns = [
	path('', views.products, name='products'),
	path('', views.front_page, name='front_page'),
	#path('products/', Products.as_view(), name='products'),
	path('product/<slug:slug>/', views.product, name='product'),

	path('category/<slug:slug>/', views.category, name='category'),
	path('all-categories/', views.all_categories, name='all_categories'),
	path('orders/', views.orders, name='orders'),
	path('order/<int:pk>/', views.order, name='order'),

	path('edit-order/<int:pk>/', views.edit_order, name='edit_order'),
	path('checkout/<int:pk>/', views.checkout, name='checkout'),

	path('decrement-cart-item-quantity/<int:pk>/', views.decrement_cart_item_quantity, name='decrement_cart_item_quantity'),
	path('increment-cart-item-quantity/<int:pk>/', views.increment_cart_item_quantity, name='increment_cart_item_quantity'),

	path('add-single-product-to-cart/<int:pk>/', views.add_single_product_to_cart, name='add_single_product_to_cart'),
	path('add-variation-product-to-cart/<int:pk>/', views.add_variation_product_to_cart, name='add_variation_product_to_cart'),

	path('cart/', views.cart, name='cart'),
	path('cart-summary/', views.cart_summary, name='cart_summary'),

	path('remove-order-item-from-cart/<int:pk>/', views.remove_order_item_from_cart, name='remove_order_item_from_cart'),

	path('process-coupon/<int:pk>/', views.process_coupon, name='process_coupon'),
	path('process-payment/<int:pk>/', views.process_payment, name='process_payment'),

	path('returns/', views.returns , name='returns'),
	path('refunds/', views.refunds , name='refunds'),

	path('cancel-order/<int:pk>/', views.cancel_order , name='cancel_order'),
	path('testing/', views.testing, name='testing'),
	path('search/', views.search, name='search'),

	path('addresses/', views.addresses, name='addresses'),
	path('add_address/', views.add_address, name='add_address'),

	path('edit-address/<int:pk>/', views.edit_address, name='edit_address'),
	path('delete-address/<int:pk>/', views.delete_address, name='delete_address'),

	path('payments/', views.payments, name='payments'),

	path('add_payment/', views.add_payment, name='add_payment'),
	path('delete-payment-method/<int:pk>/', views.delete_payment_method, name='delete_payment_method'),
	path('edit-payment-method/<int:pk>/', views.edit_payment_method, name='edit_payment_method'),

	path('quick-view/<slug:slug>/', views.quick_view, name='quick_view'),

	path('like-product/<int:pk>/', views.like_product, name='like_product'),
	path('unlike-product/<int:pk>/', views.unlike_product, name='unlike_product'),

	path('brands/', views.brands, name='brands'),
	path('brand/<slug:slug>/', views.brand, name='brand'),

	path('wishlists/', views.wishlists, name='wishlists'),
	path('wishlist/<int:pk>/', views.wishlist, name='wishlist'),
	path('create-wishlist/', views.create_wishlist, name='create_wishlist'),
	path('delete-wishlist/<int:pk>/', views.delete_wishlist, name='delete_wishlist'),
	path('delete-item-from-wishlist/<int:pk>/', views.remove_item_from_wishlist, name='remove_item_from_wishlist'),
	path('add-item-from-wishlist/<int:pk>/', views.add_item_from_wishlist, name='add_item_from_wishlist'),

	
]

