import datetime
from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
# from django.http import HttpResponseRedirect
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.utils.timezone import now
# from .models import ClassName, User, Booking
# from .forms import UserForm, BookingForm

# # Checking the classes that got booked
# total_classes = ClassName.objects.filter(booking__status='Available').count()
# booked_places = Booking.objects.values('places').count()

# # Removing the booked places with the total available seats
# classes_remaining = total_classes - booked_places

def main_page(request):
    return render(request, 'golf/index.html')

def login_page(request):
    return render(request, 'golf/login.html')
