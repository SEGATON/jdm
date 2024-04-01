from django.urls import path, include
from . import views  
from .views import CartView
app_name = 'ds_mp_app'

urlpatterns = [
    
    path('', views.front_page, name='front_page'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_conditions, name='terms_conditions'),
    path('do-not-sell-my-personal-information/', views.do_not_sell_my_personal_information, name='do_not_sell_my_personal_information'),
    path('dropshipper-application/', views.dropshipper_application, name='dropshipper_application'),
    path('f-a-q/', views.f_a_q, name='f_a_q'),
    
    path('policies/', views.policies, name='policies'),
    path('private-labelleing/', views.private_labelleing, name='private_labelleing'),
    path('for-businesses/', views.for_businesses, name='for_businesses'),
    path('careers/', views.careers, name='careers'),
    path('affiliation-program/', views.affiliation_program, name='affiliation_program'),
    path('help-center/', views.help_center, name='help_center'),



    path('category/<slug:slug>/', views.category, name='category'),



    path('brands/', views.brands, name='brands'),
    path('brand/<slug:slug>/', views.brand, name='brand'),


    path('products/', views.products, name='products'),
    #path('product/<slug:slug>/', views.product, name='product'),
    path('single-product/<slug:slug>/', views.single_product, name='single_product'),\
    path('variable-product/<slug:slug>/', views.variable_product, name='variable_product'),

    path('orders/', views.orders, name='orders'),
    path('order/<int:pk>/', views.order, name='order'),



    path('dropship-single-product/<slug:slug>/', views.dropship_single_product, name='dropship_single_product'),
    path('dropship-variable-product/<slug:slug>/', views.dropship_variable_product, name='dropship_variable_product'),

    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove-item-from-cart/<slug:slug>/', views.remove_item_from_cart, name='remove_item_from_cart'),
    path('remove-single-item-from-cart/<slug:slug>/', views.remove_single_item_from_cart, name='remove_single_item_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('request-refund/<int:pk>/', views.request_refund, name='request_refund'),
    path('refund-requests/', views.refund_requests, name='refund_requests'),
    path('refund-request/<int:pk>/', views.refund_request, name='refund_request'),
]



























