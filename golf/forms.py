"""Imports"""
from datetime import date
from django import forms
from django.conf import settings
from .models import Customer, Booking

today = date.today()


class CustomerForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Customer
        fields = ('username', 'email',)


class BookingForm(forms.ModelForm):
    requested_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMAT)

    class Meta:
        model = Booking
        fields = ('class_name', 'requested_date')
