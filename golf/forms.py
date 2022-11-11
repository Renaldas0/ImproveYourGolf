"""Imports"""
from datetime import date
from django import forms
from django.conf import settings
from .models import Customer, Booking, ClassName


today = date.today()


class CustomerForm(forms.ModelForm):
    class Meta:
        """Customer Form """
        model = Customer
        fields = ('user_name', 'email',)


class BookingForm(forms.ModelForm):
    """ The Booking Form Model """
    requested_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMAT)

    class Meta:
        """Booking form field"""
        model = Booking
        fields = ('class_name', 'requested_date',)
