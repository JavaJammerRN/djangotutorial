from django import forms
from django.forms import widgets
from .models import Booking

# this is a custom form with one element. a 'charField or textbox...' called user name. added widget for placeholder.
class SearchBookingForm(forms.Form):
	user_name = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'username'}), max_length=140)

# this is a form based off of a model. in this case it takes everythig from the booking model
class CreateBookingForm(forms.ModelForm):
	class Meta:
		model = Booking
		fields = '__all__'

