from django.contrib import admin
from doctor.models import *


# Register your models here.
class doctorDisplay(admin.ModelAdmin):
  list_display= ['user', 'dob', 'sex']

admin.site.register(Department)
admin.site.register(Doctor, doctorDisplay)