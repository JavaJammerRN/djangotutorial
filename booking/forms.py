from django import forms
from django.forms import widgets
from .models import Booking
from django.contrib.admin import widgets

# this is a custom form with one element. a 'charField or textbox...' called user name. added widget for placeholder.
class SearchBookingForm(forms.Form):
    user_name = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'username'}), max_length=140)

# this is a form based off of a model. in this case it takes everythig from the booking model
# Also added the widgets part to add class to 'date' so I can add a datetimepicker. (see personal/static/vendor/test.js)
class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class':'date'}),
        }

