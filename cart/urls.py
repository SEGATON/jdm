from django.urls import path
from . import views  

app_name = 'cart'

urlpatterns = [
	path('', views.front_page, name='front_page'),


]

