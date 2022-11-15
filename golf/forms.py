"""Imports"""
from datetime import datetime
from django import forms
from .models import Customer, ClassName, Booking
from django.urls import reverse_lazy
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.conf import settings


class BookingForm(ModelForm):

    # Model for Booking form
    CLASS_CHOICES = (
        (1, 'Short game'),
        (2, 'Kids club'),
        (3, 'Long game'),
    )

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'hx-get': reverse_lazy('booking'),
        'hx-trigger': 'keyup'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'hx-get': reverse_lazy('booking'),
        'hx-trigger': 'keyup'
    }))
    email = forms.CharField()
    lesson = forms.ChoiceField(choices=CLASS_CHOICES)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date()}))

    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'email', 'lesson', 'date']
