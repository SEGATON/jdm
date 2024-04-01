from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Article
from .models import Category




# Create your views here.



def front_page(request):
	return render(request, 'blog/front_page.html', {
		
		})

def articles(request):
	articles = Article.objects.all()
	return render(request, 'blog/articles.html', {
			'articles':articles
		})

def article(request, article):
	article = get_object_or_404(Article, slug=article)
	category = article.category

	return render(request, 'blog/article.html', {
			'article':article,
			'category':category,

		})


def categories(request):

	return {
		'categories':Category.objects.all()
	}
	
def category(request, slug):
	category = get_object_or_404(Category, slug=slug)

	return render(request, 'blog/category.html', {
			'category':category
		})
