from django.forms import ModelForm
from django import forms
from .models import *

class DoctorForm(ModelForm):
    class Meta:
        model=Doctor
        fields=['dob','sex','specialization','avatar','Bio','Awards']