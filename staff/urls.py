from django.urls import path
from .views import *

urlpatterns=[
    path('doctor/<int:doctor_id>/availability/', doctor_availability, name='doctor_availability'),
]

