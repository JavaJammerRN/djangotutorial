from django.shortcuts import render
from .models import Booking
from .forms import SearchBookingForm

def booking(request):
    booking_list = Booking.objects.all()
    form = SearchBookingForm()
    context = {'booking_list' : booking_list, 'form' : form}
    return render(request, 'booking/booking.html', context)