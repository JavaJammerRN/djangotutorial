from django import forms
from django.forms import widgets
from .models import Booking


class SearchBookingForm(forms.Form):
	user_name = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'username'}), max_length=140)

class CreateBookingForm(forms.ModelForm):
	class Meta:
		model = Booking
		fields = '__all__'

