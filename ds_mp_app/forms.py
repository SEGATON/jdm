from django import forms

from .models import Refunds





class RequestRefund(forms.ModelForm):
	class Meta:
		model = Refunds
		fields = ['reason_for_refund']

	