from django import forms

from .models import Person



class AddPersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = '__all__'
		exclude = ['user','followers','likes','faves','saved']

class EditPersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = '__all__'
		exclude = ['user','followers','likes','faves','saved']