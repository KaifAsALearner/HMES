from django.urls import path
from .views import *

urlpatterns = [
    path('book/<int:doctor_id>/', book_appointment, name='book_appointment'),
]
