from django.forms import ModelForm
from django import forms
from .models import *
from appointment.models import Appointment

class DoctorForm(ModelForm):
    class Meta:
        model=Doctor
        fields=['dob','sex','specialization','avatar','Bio','Awards']
class NoteForm(ModelForm):
    class Meta:
        model=Appointment
        fields=['doctorsnote']