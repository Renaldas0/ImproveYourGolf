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