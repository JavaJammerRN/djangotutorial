from django.shortcuts import render
from .models import Booking
from .forms import SearchBookingForm, CreateBookingForm
from django.contrib import messages


def booking_create(request):
    booking_form = CreateBookingForm()
    context = {'form' : booking_form}

    if request.method == 'POST':
        form = CreateBookingForm(request.POST)

        if form.is_valid():
            booking = form.save()
            messages.success(request, 'Booking has been created!')

        else:
            messages.warning(request, 'Oops, Something went wrong. Please try again later!')
            form = CreateBookingForm() # An unbound form

    return render(request, 'booking/bookingcreate.html', context)

def booking(request):
    booking_form = SearchBookingForm()
    context = {'form' : booking_form}

    if request.method == 'POST':
        form = SearchBookingForm(request.POST)

        if form.is_valid():
            user_name = form.cleaned_data['user_name']

            booking_list = Booking.objects.filter(user__user_name= user_name)

            if not booking_list:
                messages.warning(request, 'User <strong>' + user_name + ' </strong> does not exist!')
            else:
                context['booking_list'] = booking_list

        else:
            form = SearchBookingForm() # An unbound form


    return render(request, 'booking/booking.html', context)


def booking_detail(request, pk):

    booking = Booking.objects.get(id = pk)
    context = {'booking' : booking}
    print(booking.date)
    return render(request, 'booking/bookingdetail.html', context)

