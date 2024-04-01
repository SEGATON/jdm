from django.db import models

# Create your models here.
from django.conf import settings
from ecommerce.models import Product 

class Vendor(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='ds_mp_vendor')
	vendor_title = models.CharField(max_length=100)
	vendor_descripton = models.TextField(max_length=2000, null=True, blank=True)
	vendor_logo = models.ImageField(default='media/DS_MP_APP/VENDORS/VENDORS_LOGOS/default.jpg', upload_to='media/DS_MP_APP/VENDORS/VENDORS_LOGOS/', null=True, blank=True  )
	vendor_cover_image = models.ImageField(default='media/DS_MP_APP/VENDORS/VENDORS_LOGOS/cover-image-default.jpg', upload_to='media/DS_MP_APP/VENDORS/VENDORS_COVER_IMAGES/', null=True, blank=True  )
	vendor_products = models.ManyToManyField(Product, null=True, blank=True )

	vendor_phone = models.CharField(max_length=100)
	vendor_email = models.EmailField(max_length=100)
	vendor_website_URL = models.URLField(max_length=100)

	def __str__(self):
		return self.vendor_title