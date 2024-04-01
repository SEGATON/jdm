from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

from accounts.models import CustomUser
from django.shortcuts import reverse


from treebeard.mp_tree import MP_Node


class GalleryImage(models.Model):
	gallery_image = models.ImageField(upload_to='media/BLOG_POST/GALLERY_IMAGES/')



class Gallery(models.Model):
	title = models.CharField(max_length=255, blank=True,null=True)
	gallery_image = models.ManyToManyField(GalleryImage, null=True, blank=True)



	def __str__(self):  
		return self.title


class Category(MP_Node): 
	 title =models.CharField(max_length=300)
	 slug =models.SlugField(max_length=300)

	 def get_absolute_url(self):
	 	return reverse('blog:category', args=[self.slug])

	 def __str__(self):
	 	return self.title


class Article(models.Model):

	options = (('draft','Draft',),('published','Published'))

	title = models.CharField(max_length=300)
	slug = models.SlugField(max_length=300)

	category = models.ManyToManyField(Category, blank=True, null=True)

	introduction = RichTextField(max_length=30000)
	main_paragraph = RichTextField(max_length=30000)
	conclusion = RichTextField(max_length=30000)

	author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)

	date_published = models.DateTimeField(auto_now_add=True, null=True)
	date_updated = models.DateTimeField()

	status = models.CharField(max_length=10, choices=options, default='draft')

	featured_image = models.ImageField(upload_to='media/BLOG_POST/FEATURED_IMAGES/', null=True, blank=True)

	#gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True,blank=True)

	class Meta:
		ordering = ('-date_published',)

	def get_absolute_url(self):
		return reverse('blog:article', args=[self.slug])

	def __str__(self):
		return str(self.title)