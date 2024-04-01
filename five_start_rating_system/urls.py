from django.urls import path
from . import views  

app_name = 'five_start_rating_system'

urlpatterns = [
	path('', views.front_page, name='front_page'),
	path('process_review/', views.process_review, name='process_review'),
	
]
