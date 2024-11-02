from django.urls import path
from . import views

urlpatterns=[
    path('doctor/',views.doctor,name="doctor"),
    path('doctor-dashboard/',views.doctor,name="doctor-dashboard"),
    path('doctor-profile/<str:pk>/',views.doctor_profile,name="doctor-profile"),
    path('doctor-update/<str:pk>/',views.doctor_update,name="doctor-update"),
    path('doctor-dashboard/<str:pk>/',views.doctor_dashboard,name="doctor-dashboard"),
    path('appointment-overview/<str:pk>/',views.appointment_overview,name="appointment-overview"),
    path('doctor-note/<int:pk>/',views.doctor_note,name="doctor-note"),
    path('doctor-feedback/<int:pk>/',views.doctor_feedback,name="doctor-feedback")
]