
from django import forms  

from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from localflavor.us.forms import USStateSelect
from localflavor.us.forms import USZipCodeField
from localflavor.us.forms import USSocialSecurityNumberField

from localflavor import generic


class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
	class Meta:
		fields = '__all__'


class CreateAccountForm(UserCreationForm):
	ACCOUNT_TYPE = [
		("vendor_account", "Vendor account"),
		("dropshipper_account", "Dropshipper account"),
		("vendor_dropshipper_account", "Vendor and dropshipper account"),
	]

	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email address'}))

	account_type = forms.CharField(widget=forms.Select(choices=ACCOUNT_TYPE, attrs=
		{'class':'form-select'}))

	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Create password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}))
	class Meta:
		model = CustomUser
		fields = ['username','email','account_type','password1','password2']


class ChangeUsernameForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['username']


class ChangePhoneNumberForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['phone_number']


class VendorApplicationForm(forms.ModelForm):
	ssn = USSocialSecurityNumberField()
	legal_business_state = USStateSelect(attrs=None)
	legal_business_zip_code = USZipCodeField()
	d_b_a = forms.CharField(label='Doing business as',widget=forms.TextInput(attrs=None))
	ssn = forms.CharField(label='Social security number',widget=forms.TextInput(attrs=None))




	class Meta:
		model = CustomUser
		fields = [
			'first_name',
			'last_name',


			'email',
			'phone_number',
			'legal_business_phone_number',

			'type_of_business',

			'business_lega_name',
			'd_b_a',

			'legal_business_address_line_1',
			'legal_business_address_line_2',
			'legal_business_unit',
			'legal_business_city',

			'legal_business_state',
			'legal_business_zip_code',

			'tax_ID',

			'ssn',




		]