from django.contrib import admin
from .models import Article
from .models import Category

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}




class CategoryAdmin(TreeAdmin):
	list_display = ['title','slug']
	prepopulated_fields = {
		'slug':('title',)
	}
	form = movenodeform_factory(Category)


admin.site.register(Category, CategoryAdmin)