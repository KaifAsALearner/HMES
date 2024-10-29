from django.urls import path
from . import views

urlpatterns=[
    path('doctor/',views.doctor,name="doctor"),
    path('doctor_dashboard/',views.doctor,name="doctor_dashboard"),
]