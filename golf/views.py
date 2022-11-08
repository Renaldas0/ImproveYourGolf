import datetime
from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.timezone import now
from .models import ClassName, Customer, Booking
from .forms import CustomerForm, BookingForm


def main_page(request):
    return render(request, 'golf/index.html')


def booking_view(request):
    """ Order the data by the date closest to the current \
    date only for dates in the future, not for dates that \
    have passed
    """

    # Show the current and upcoming dates
    today = now().date()
    classes = ClassName.objects.all()
    booking_list = Booking.objects.filter(booking_date__gte=today).order_by('requested_date')


def get_customer_instance(request, User):
    """ Returns customer instance if User is logged in """
    customer_email = request.user.email
    customer = Customer.objects.filter(email=customer_email).first()

    return 


def check_availabilty(customer_class_name, customer_requested_date):
    """ Check availability against Booking model using customer input """

    # Check to see how many classes exist at that date
    classes_booked = len(Booking.objects.filter(
        class_name=customer_class_name,
        requested_date=customer_requested_date, status="Available"))

    # Return number of classes
    return classes_booked
