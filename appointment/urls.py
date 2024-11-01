from django.urls import path
from .views import *

urlpatterns=[
  path('bookanappt/', bookanappt, name="bookanappt")
]