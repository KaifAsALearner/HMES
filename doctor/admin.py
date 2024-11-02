from django.contrib import admin
from doctor.models import *


# Register your models here.
class doctorDisplay(admin.ModelAdmin):
  list_display= ['user', 'dob', 'sex']

class displayAppointmentSlot(admin.ModelAdmin):
  list_display= ['id', 'doctor', 'day_of_week', 'session', 'max_bookings']

admin.site.register(Department)
admin.site.register(Doctor, doctorDisplay)
admin.site.register(AppointmentSlot, displayAppointmentSlot)