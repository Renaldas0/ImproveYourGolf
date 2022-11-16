"""Imports"""
from datetime import datetime
from django import forms
from django.urls import reverse_lazy
from django.forms import ModelForm
from django.conf import settings
from .models import Customer, Booking


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'email',)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('class_name',)
