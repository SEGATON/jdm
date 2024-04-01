from django.urls import path
from . import views  

app_name = 'blog'

urlpatterns = [
	path('', views.front_page, name='front_page'),
	path('articles/', views.articles, name='articles'),
	path('article/<slug:article>/', views.article, name='article'),
	path('category/<slug:slug>/', views.category ,name='category')
]
