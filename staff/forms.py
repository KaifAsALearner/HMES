from django.forms import ModelForm
from django import forms
from hospital_test.models import Test

class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'descript']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your name'
            }),
            'descript': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a description',
                'rows': 4,
            }),
        }