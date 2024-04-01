from django.db import models

# Create your models here.


from accounts.models import CustomUser





### PERSON OBJECT STARTS ########################################################################################


class Person(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='person_user')
	
	first_name = models.CharField(max_length=50, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	biography = models.TextField(max_length=500, null=True, blank=True)

	followers = models.ManyToManyField(CustomUser, related_name='person_followers',  null=True, blank=True)
	likes = models.ManyToManyField(CustomUser, related_name='person_likes',  null=True, blank=True)
	faves = models.ManyToManyField(CustomUser, related_name='person_faved',  null=True, blank=True)
	saved = models.ManyToManyField(CustomUser, related_name='person_saved',  null=True, blank=True)




	

### PERSON OBJECT ENDS ##########################################################################################