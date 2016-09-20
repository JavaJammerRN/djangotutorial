from django import forms
from django.forms import widgets


class SearchBookingForm(forms.Form):
	user_name = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'username'}), max_length=140)