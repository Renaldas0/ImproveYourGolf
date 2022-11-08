from django import forms


class AvailabilityForm(forms.Form):
    lesson = forms.ChoiceField(choices=LESSONS)
