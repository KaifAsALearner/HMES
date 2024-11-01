from django.urls import path
from .views import *

urlpatterns=[
    path('patient-dashboard/', patient_db, name="patient_db"),
    path('addapatient/', addapatient, name="addapatient"),
]