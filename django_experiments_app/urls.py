from django.urls import path
from . import views  

app_name = 'django_experiments_app'

urlpatterns = [
	path('', views.front_page, name='front_page'),
	path('persons/', views.persons, name='persons'),
	path('person/<int:pk>/', views.person, name='person'),
	path('add-person/', views.add_person, name='add_person'),
	path('edit-person/<int:pk>/', views.edit_person, name='edit_person'),
	path('delete-person/<int:pk>/', views.delete_person, name='delete_person'),
	path('recipe-maker/', views.recipe_maker, name='recipe_maker'),
]
