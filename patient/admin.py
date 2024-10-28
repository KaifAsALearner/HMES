from django.contrib import admin
from .models import *

# Register your models here.
class patientDisplay(admin.ModelAdmin):
  list_display= ['user', 'first_name', 'last_name', 'dob', 'sex']


admin.site.register(Patient, patientDisplay)

