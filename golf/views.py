import datetime
from .models import Customer
from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.timezone import now
from .forms import CustomerForm, BookingForm


def main_page(request):
    return render(request, 'golf/index.html')


def booking(request):
    customers = Customer.objects.all()
    context = {
        'customer_form': CustomerForm(),
        'booking_form': BookingForm()
    }
    return render(request, 'golf/booking.html', context)
