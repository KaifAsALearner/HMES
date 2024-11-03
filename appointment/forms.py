from django import forms
from django.forms import ModelForm
from appointment.models import Appointment

class FeedbackForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['feedback']
        widgets = {
            'feedback': forms.Textarea(attrs={
                'class': 'form-control',  
                'rows': 4,                
                'placeholder': 'Enter your feedback here...'  
            }),
        }