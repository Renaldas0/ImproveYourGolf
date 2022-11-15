import datetime
from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.timezone import now
from .forms import BookingForm


def main_page(request):
    return render(request, 'golf/index.html')


def booking(request):
    context = {'form': BookingForm()}
    return render(request, 'golf/booking.html', context)


def delete_booking(request):
    return render(request, 'golf/delete_booking.html')


def get_customer_instance(request, User):
    """ Returns customer instance if User is logged in """
    customer_email = request.user.email
    customer = Customer.objects.filter(email=customer_email).first()

    return customer


def check_availabilty(customer_class_name, customer_requested_date):
    """ Check availability against Booking model using customer input """

    # Check to see how many classes exist at that date
    classes_booked = len(Booking.objects.filter(
        class_name=customer_class_name,
        requested_date=customer_requested_date, status="Available"))

    # Return number of classes
    return classes_booked
