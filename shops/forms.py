from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import Item, Images

PAYMENT_CHOICES = (
	('S', 'Stripe'),
	('P', 'PayPal'),
	('M', 'M-pesa')

)

class CheckoutForm(forms.Form):
	street_address = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control'
		}))
	apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
		'class': 'form-control'
		}))
	county = forms.CharField(required=False, widget=forms.TextInput(attrs={
		'class': 'form-control'
		}))
	phone = forms.CharField(required=False, widget=forms.NumberInput(attrs={
		'class': 'form-control'
		}))
	zip = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'custom-select d-block w-100',
		'id': 'zip'
		}))
	same_shipping_address = forms.BooleanField(required=False)
	save_info = forms.BooleanField(required=False	)
	payment_option = forms.ChoiceField(
		widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
	code = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Promo code',
		'aria-label': 'Recipient\'s username',
		'aria-describedby': 'basic-addon2'
		}))

class RefundForm(forms.Form):
	ref_code = forms.CharField()
	message = forms.CharField(widget=forms.Textarea(attrs={
		'rows': 4
		}))
	email = forms.EmailField()


class PostForms(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	price = forms.CharField(widget=forms.NumberInput(attrs={
		'class':'form-control'
		}))
	discount_price = forms.CharField(widget=forms.NumberInput(attrs={
		'class':'form-control'
		}))
	size = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))

	color = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	type_cloth = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	slug = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	description = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control'
		}))
	
	class Meta:
		model = Item
		fields = [
			"category",
			"title",
			"price",
			"discount_price",
			"size",
			"color",
			"type_cloth",
			"label",
			"slug",
			"description",
			"image",
	

		]
class ImageForms(forms.ModelForm):
	image = forms.ImageField(label='Image')

	class Meta:
		model = Images
		fields = ('image',)