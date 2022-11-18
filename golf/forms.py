"""Imports"""
from datetime import datetime
from django import forms
from django.forms import ModelForm
from django.conf import settings
from .models import Customer, Booking

today = datetime.today


class CustomerForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Customer
        fields = ('name', 'email',)


class BookingForm(forms.ModelForm):
    requested_date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'min': datetime.now().date()}))

    class Meta:
        model = Booking
        fields = ('class_name', 'requested_date')
