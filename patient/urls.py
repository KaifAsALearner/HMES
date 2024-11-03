from django.urls import path
from .views import *

urlpatterns=[
    path('patient-dashboard/<int:chosenfield>/', patient_db, name="patient_db"),
    path('addapatient/', addapatient, name="addapatient"),
    path('doctorsnote/<int:apt_id>/', doctorsnote, name='doctorsnote'),
]