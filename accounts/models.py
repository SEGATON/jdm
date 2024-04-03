from django.db import models

from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
from django.utils.translation import gettext_lazy as _ 


from localflavor.us.models import USStateField
from localflavor.us.models import USZipCodeField
from localflavor.us.models import USPostalCodeField
from localflavor.us.models import USSocialSecurityNumberField


class CustomUserManager(BaseUserManager):
	def create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError("Email nich gut")
		email 		= self.normalize_email(email)
		user 		= self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save() 

		return user

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError(_("ffffffffffff"))
		if extra_fields.get('is_superuser') is not True:
			raise ValueError(_("dddddddd"))
		return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
	ACCOUNT_TYPE = (
			('starter','Starter'),
			('vendor_account','Vendor account'),
			('dropshipper_account','Dropshipper account'),
			('vendor_and_dropshipper','Vendor and dropshipper'),
		)
	account_type 			= models.CharField(max_length=300, choices=ACCOUNT_TYPE, null=True, blank=True)

	email 			= models.EmailField(_("email address"), unique=True)
	phone_number 			= models.CharField(max_length=100,null=True,blank=True)

	business_lega_name 		= models.CharField(max_length=100,null=True,blank=True)
	d_b_a 			= models.CharField(max_length=100,null=True,blank=True)

	TYPE_OF_BUSINESS = (
			('sole_proprietor','Sole Proprietor'),
			('limited_liability_company','Limited Liability Company'),
			('c_corp','C Corporation'),
			('s_corp','S Corporation'),
			('non_profit','Nonprofit'),

		)

	type_of_business 		= models.CharField(choices=TYPE_OF_BUSINESS, max_length=100, null=True, blank=True)

	legal_business_address_line_1 	= models.CharField(max_length=100,null=True,blank=True)
	legal_business_address_line_2 	= models.CharField(max_length=100,null=True,blank=True)
	legal_business_unit 		= models.CharField(max_length=100,null=True,blank=True)
	legal_business_city 		= models.CharField(max_length=100,null=True,blank=True)
	legal_business_state 		= USStateField()
	legal_business_zip_code 		= USZipCodeField()
	legal_business_phone_number		= models.CharField(max_length=100,null=True,blank=True)
	legal_business_email 		= models.CharField(max_length=100,null=True,blank=True)

	tax_ID = models.CharField(max_length=100, null=True, blank=True)
	ssn = models.CharField(max_length=100, null=True, blank=True)

	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)

	USERNAME_FIELD 		= "email"
	REQUIRED_FIELDS 		= ["username"]

	objects 			= CustomUserManager()

	APPLICATION_STATUS = (
			('under_review','Under review'),
			('pending','Pending'),
			('active','Active'),
			('suspended','Suspended'),
			('terminated','Terminated'),
		
		)

	application_status = models.CharField(max_length=100, choices=APPLICATION_STATUS, null=True, blank=True)



