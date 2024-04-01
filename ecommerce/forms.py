from .models import Order
from .models import Payment
from .models import Address
from memberships.models import Profile

from django import forms

from localflavor.us.forms import USStateSelect
from localflavor.us.forms import USZipCodeField

from .models import Newsletters
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Wishlist
class EditOrder(forms.ModelForm):
	class Meta:
		model = Order 
		fields = '__all__'
		exclude = ['user']


class AddPaymentMethod(forms.ModelForm):


	CARD_TYPE = (
			('visa','VISA'),
			('mastercard','MasterCard'),
			('american_express','American Express'),
			('discover','Discover'),
		)
	
	PAYMENT_METHOD = (
		('bank_account','Bank account'),
		('credit_or_debit_card','Credit or debit card'),
		('paypal','PayPal'),
	)

	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'first name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'last name'}))
	payment_method = forms.CharField(widget=forms.Select(choices=PAYMENT_METHOD ,attrs={'class':'custom_tf','placeholder':' payment method'}))
	card_number= forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'card number'}))
	expiration_date= forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':' expi date' , 'type':'date'}))
	security_code= forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'sec code'}))
	zip_code= forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'zip code'}))
	card_type= forms.CharField(widget=forms.Select(choices=CARD_TYPE, attrs={'class':'custom_tf','placeholder':' card type'}))
	set_to_default= forms.CharField(widget=forms.CheckboxInput(attrs={}))

	class Meta:
		model = Payment 
		fields = '__all__'
		


class EditPaymentMethod(forms.ModelForm):


	CARD_TYPE = (
			('visa','VISA'),
			('mastercard','MasterCard'),
			('american_express','American Express'),
			('discover','Discover'),
		)
	
	PAYMENT_METHOD = (
		('bank_account','Bank account'),
		('credit_or_debit_card','Credit or debit card'),
		('paypal','PayPal'),
	)

	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'first name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'last name'}))
	
	payment_method = forms.CharField(widget=forms.Select(choices=PAYMENT_METHOD ,attrs={'class':'custom_tf','placeholder':' payment method'}))
	card_number= forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'card number'}))
	expiration_date= forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':' expi date' , 'type':'date'}))
	security_code= forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'sec code'}))
	zip_code= forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'zip code'}))
	
	card_type= forms.CharField(widget=forms.Select(choices=CARD_TYPE, attrs={'class':'custom_tf','placeholder':' card type'}))
	
	set_to_default= forms.CharField(widget=forms.CheckboxInput(attrs={}))

	class Meta:
		model = Payment 
		fields = '__all__'


class AddAddressForm(forms.ModelForm):

	TYPE_OF_ADDRESS = (
				('billing_address','Billing address'),
				('shipping_address','Shipping address'),
				('p_o_box_number','Post office box number'),
			)
	type_of_address = forms.CharField(widget=forms.Select(choices=TYPE_OF_ADDRESS, attrs={'class':'custom_tf','placeholder':'last name'}))
	
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'first name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'last name'}))
	
	street_name_01 = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'steet line 1'}))
	street_name_02 = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'street line 2'}))
	street_city = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'city'}))
	street_state = forms.CharField(widget=USStateSelect(attrs={'class':'custom_tf','placeholder':'state'}))
	street_zip_code = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'zip code'}))
	
	default_address = forms.CharField(widget=forms.CheckboxInput(attrs={}))
	
	date_created = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'last name', 'type':'date'}))

	phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'phone number'}))
	
	address_id_name = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'address id '}))

	class Meta:
		model = Address 
		fields = '__all__'


		
class EditAddressForm(forms.ModelForm):

	TYPE_OF_ADDRESS = (
				('billing_address','Billing address'),
				('shipping_address','Shipping address'),
				('p_o_box_number','Post office box number'),
			)
	type_of_address = forms.CharField(widget=forms.Select(choices=TYPE_OF_ADDRESS, attrs={'class':'custom_tf','placeholder':'last name'}))
	
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'first name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'last name'}))
	
	street_name_01 = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'steet line 1'}))
	street_name_02 = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'street line 2'}))
	street_city = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'city'}))
	street_state = forms.CharField(widget=USStateSelect(attrs={'class':'custom_tf','placeholder':'state'}))
	street_zip_code = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'zip code'}))
	
	default_address = forms.CharField(widget=forms.CheckboxInput(attrs={}))
	
	date_created = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'last name', 'type':'date'}))

	phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'phone number'}))
	
	address_id_name = forms.CharField(widget=forms.TextInput(attrs={'class':'custom_tf','placeholder':'address id '}))

	class Meta:
		model = Address 
		fields = '__all__'



class NewslettersSubscriptionForm(forms.ModelForm):
	email_address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email address'}))
	class Meta:
		model = Newsletters
		fields = '__all__'
		exclude = ['slug','title','first_name','last_name','phone_number']




class CreateWishlistForm(forms.ModelForm):
	class Meta:
		model = Wishlist
		fields = '__all__'
		exclude = ['user']



class CustomWLMenu(forms.ModelMultipleChoiceField):

	def label_from_instance(self, user):

		return "%s" % user 	

class AddToWishlistForm(forms.ModelForm):

	wishlists = CustomWLMenu(queryset=Wishlist.objects.filter(), widget=forms.CheckboxSelectMultiple)

	class Meta:
		model = Profile
		fields = ['wishlists']