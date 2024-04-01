"""
URL configuration for django_experiments project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_experiments_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('blog/', include('blog.urls')),
    path('ds_mp_app/', include('ds_mp_app.urls')),
    path('ecommerce/', include('ecommerce.urls')),
    path('five_start_rating_system/', include('five_start_rating_system.urls')),    

    path('memberships/', include('memberships.urls')),
    path('comments/', include('django_comments_xtd.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('paypal/', include("paypal.standard.ipn.urls")),

    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('advanced_filters/', include('advanced_filters.urls')),

    path('cart/', include('cart.urls')),
    path('customers/', include('customers.urls')),
    path('payments/', include('payments.urls')),
    path('checkout/', include('checkout.urls')),
    path('orders/', include('orders.urls')),
    path('addresses/', include('addresses.urls')),
    path('vendors/', include('vendors.urls')),

    path('messages/', include('postman.urls')),
    path('herald/', include('herald.urls')),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)