from django.urls import path
from .views import *

urlpatterns = [
    path('book/<int:doctor_id>/', book_appointment, name='book_appointment'),
    path('update-feedback/<int:pk>/', update_feedback, name='update-feedback'),
    path('cancelappointment/<int:apt_id>/', cancelappointment, name='canapt'),
    path('completeappointment/<int:apt_id>/', completeappointment, name='comapt'),
]