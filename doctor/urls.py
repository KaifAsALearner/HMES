from django.urls import path
from . import views

urlpatterns=[
    path('doctor/',views.doctor,name="doctor"),
    path('doctor-dashboard/',views.doctor,name="doctor-dashboard"),
    path('doctor-profile/<str:pk>/',views.doctor_profile,name="doctor-profile"),
    path('doctor-update/<str:pk>/',views.doctor_update,name="doctor-update")
]