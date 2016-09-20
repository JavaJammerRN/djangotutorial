from django import forms


class SearchBookingForm(forms.Form):
	user_name = forms.CharField(max_length=140)