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


def booking(request):

    customer_form = CustomerForm(request.POST or None)
    if customer_form.is_valid():
        customer_form.save()
        return HttpResponseRedirect("")
    context = {
        "customer_form": customer_form
    }

    return render(request, 'golf/booking.html', context)


def customer(request):

    booking_form = BookingForm(request.POST or None)
    if booking_form.is_valid():
        booking_form.save()
        messages.success(request, "Booking successful")
        return HttpResponseRedirect("")
    context = {
        "booking_form": booking_form
    }

    return render(request, 'golf/booking.html', context)


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
