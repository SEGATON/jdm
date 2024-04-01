from django.urls import path
from . import views  
from .views import PublicProfile
app_name = 'memberships'

urlpatterns = [
	path('', views.profile, name='profile'),
	path('edit_profile/<int:pk>/', views.edit_profile, name='edit_profile'),
	path('delete_profile/<int:pk>/', views.delete_profile, name='delete_profile'),
	path('follow-profile/<int:pk>/', views.follow_profile, name='follow_profile'),

	path('public-profile/<int:pk>/', PublicProfile.as_view(), name='public_profile')


]
