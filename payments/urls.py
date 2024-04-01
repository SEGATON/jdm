from django.urls import path
from . import views  

app_name = 'payments'

urlpatterns = [
	path('', views.front_page, name='front_page'),

]

