from django.db import models

from django.conf import settings
from ecommerce.models import Product
# Create your models here.
from ckeditor.fields import RichTextField
from ecommerce.models import Wishlist
from easy_thumbnails.fields import ThumbnailerImageField

class Profile(models.Model):
   
          user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
          biography = RichTextField(max_length=10000, null=True, blank=True)


          profile_photo = ThumbnailerImageField(default='/MEMBERSHIP/PROFILE_PHOTOS/default_profile_photo.png', upload_to='PROFILE_PHOTOS')

          website_url = models.URLField(max_length=1000,null=True, blank=True)
          twitter = models.URLField(max_length=1000,null=True, blank=True)
          facebook = models.URLField(max_length=1000,null=True, blank=True)
          youtube = models.URLField(max_length=1000,null=True, blank=True)
          instagram = models.URLField(max_length=1000,null=True, blank=True)

          bookmarks = models.ManyToManyField(Product, null=True, blank=True, related_name='bookmarks')

          wishlists = models.ManyToManyField(Wishlist, null=True, blank=True, related_name='wishlists')

          old_cart = models.CharField(max_length=200, blank=True, null=True)

          def __str__(self):
                    return str(self.user)




class Bookmark(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='ds_mp_product_bookmark_user')
    products = models.ManyToManyField(Product, null=True, blank=True, related_name='ds_mp_product_bookmark')