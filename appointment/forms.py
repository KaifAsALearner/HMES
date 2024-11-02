from django.forms import ModelForm
from django import forms
from .models import *
from appointment.models import Appointment

class FeedbackForm(ModelForm):
    class Meta:
        model=Appointment
        fields=['feedback']