"""Imports"""
from datetime import datetime
from django import forms
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.conf import settings


class BookingForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('booking')
        self.helper.form_method = 'GET'
        self.helper.add_input(Submit('submit', 'Submit'))

    """ The Booking Form Model """
    CLASS_CHOICES = (
        (1, 'Short game'),
        (2, 'Kids club'),
        (3, 'Long game'),
    )

    name = forms.CharField(widget=forms.TextInput(attrs={
        'hx-get': reverse_lazy('booking'),
        'hx-trigger': 'keyup'
    }))
    email = forms.CharField()
    lesson = forms.ChoiceField(choices=CLASS_CHOICES)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date()}))
