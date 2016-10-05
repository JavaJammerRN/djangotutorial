from django.conf.urls import url, include
from . import views
from django.views.generic import DetailView
from .models import Booking

# each view corresponds to a view definition in views.py
urlpatterns = [
    url(r'^$', views.booking, name='booking'),
    url(r'^(?P<pk>\d+)$', views.booking_detail, name='booking_detail'),
    url(r'^create$', views.booking_create, name='booking_create'),
]
