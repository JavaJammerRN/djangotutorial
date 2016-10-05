from django.shortcuts import render
from .models import Booking
from .forms import SearchBookingForm, CreateBookingForm
from django.contrib import messages

# booking form is created and added to context of the page (bookingcreate.html) 
def booking_create(request):
    booking_form = CreateBookingForm()
    context = {'form' : booking_form}

    return render(request, 'booking/bookingcreate.html', context)

# booking form is create and added to context (check forms.py to see how the forms were made)
# check if request is post is submitted
def booking(request):
    booking_form = SearchBookingForm()
    context = {'form' : booking_form}

    if request.method == 'POST':
        # this gets the form data
        form = SearchBookingForm(request.POST)

        # checking if form is valid againt model
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            # user__user_name is the syntaxt to filter by usernam of the user model in the booking object, filter returns a list.
            # so this gets all booking objects with the username
            booking_list = Booking.objects.filter(user__user_name= user_name)

            # if there its empty, we make message. this one is warning. there are others. see docs
            # else, create a context map called booking list with the list. this will be shown now in booking.html
            if not booking_list:
                messages.warning(request, 'User <strong>' + user_name + ' </strong> does not exist!')
            else:
                context['booking_list'] = booking_list

        else:
            form = ContactForm() # An unbound form


    return render(request, 'booking/booking.html', context)

# gets the pk from the urls.py, gets booking with that pk and displays it. pretty simple.
def booking_detail(request, pk):

    booking = Booking.objects.get(id = pk)
    context = {'booking' : booking}
    return render(request, 'booking/bookingdetail.html', context)

