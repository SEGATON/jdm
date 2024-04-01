from django.db import models

from accounts.models import CustomUser

# Create your models here.


class Rating(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	rating = models.CharField(max_length=20)
	comment = models.TextField(max_length=2000)

	date_created = models.DateTimeField(auto_now_add=True)

	#thumbs = models.IntegerField()
	thumbs_up = models.IntegerField()
	thumbs_down = models.IntegerField()