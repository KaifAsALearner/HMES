from django.contrib import admin
from .models import *

# Register your models here.
class userinfoDisplay(admin.ModelAdmin):
  list_display= ['user', 'mobile_number', 'role_def']

admin.site.register(UserInfo, userinfoDisplay)

