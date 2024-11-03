from django.forms import ModelForm
from django import forms
from django.urls import reverse_lazy
from .models import *
from appointment.models import Appointment
from datetime import date



class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['dob', 'sex', 'specialization', 'avatar', 'Bio', 'Awards']
        labels = {
            'dob': 'Date of Birth',
            'sex': 'Sex',
            'specialization': 'Specialization',
            'avatar': 'Profile Picture',
            'Bio': 'Biography',
            'Awards': 'Awards',
        }
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'max': date.today()}),  # Date input
            'sex': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for sex
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),  # Text input for specialization
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),  # File input for avatar
            'Bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # Textarea for Bio
            'Awards': forms.TextInput(attrs={'class': 'form-control'}),  # Text input for Awards
        }

class NoteForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctorsnote']
        widgets = {
            'doctorsnote': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter your notes here...'}),
        }