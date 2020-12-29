from django import forms

class Mpesaform(forms.Form):

	phone = forms.CharField(widget=forms.NumberInput(attrs={
		'class': 'form-control', 'placeholder':'254725696052'
	}))
