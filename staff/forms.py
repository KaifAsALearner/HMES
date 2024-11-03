from django.forms import ModelForm
from django import forms
from hospital_test.models import Test

class TestForm(ModelForm):
    class Meta:
        model=Test
        fields=['name','descript']