from django.shortcuts import render
from .models import Booking
from .forms import SearchBookingForm

def booking(request):
    booking_form = SearchBookingForm()
    context = {'form' : booking_form}

    if request.method == 'POST':
        form = SearchBookingForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']

            booking_list = Booking.objects.filter(user__user_name= user_name)
            context['booking_list'] = booking_list

        else:
            form = ContactForm() # An unbound form

    return render(request, 'booking/booking.html', context)


# def booking_detail(request, pk):

#     booking = Booking.objects.filter(id = pk)
#     context = {'booking' : booking}
#     return render(request, 'booking/bookingdetail.html', context)