from django.urls import path
from . import views 
from .forms import LoginForm
from django.contrib.auth import views as auth_views
app_name = 'accounts'

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('account/', views.account, name='account'),
    path('create-account/', views.create_account, name='create_account'),
    path('account-settings/', views.account_settings, name='account_settings'),
    path('privacy-settings/', views.privacy_settings, name='privacy_settings'),
    path('vendor-application/', views.vendor_application, name='vendor_application'),

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', form_class=LoginForm), name="login"),

]