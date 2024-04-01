from django.urls import path
from . import views  

app_name = 'vendors'

urlpatterns = [
	path('', views.front_page, name='front_page'),
	path('vendor_profile/<int:pk>/', views.vendor_profile, name='vendor_profile'),
	path('save-vendor/<int:pk>/', views.save_vendor , name='save_vendor'),
	path('follow-vendor/<int:pk>/', views.follow_vendor , name='follow_vendor'),
	path('set-notifications-from-vendor/<int:pk>/', views.set_notifications_from_vendor , name='set_notifications_from_vendor'),
]
