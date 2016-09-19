from django.contrib import admin

from booking.models import Booking, Desk, User

admin.site.register(Booking)
admin.site.register(Desk)
admin.site.register(User)

