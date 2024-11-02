from django.contrib import admin
from .models import *

# Register your models here.

class appointmentDisplay(admin.ModelAdmin):
  list_display= ['id', 'patient', 'date', 'stat']

admin.site.register(Appointment,appointmentDisplay)