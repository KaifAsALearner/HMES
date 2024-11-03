from django.urls import path
from .views import *

urlpatterns=[
    path('doctor/<int:doctor_id>/availability/', doctor_availability, name='doctor_availability'),
    path('staff-dashboard/<int:chosenfield>/', staff_db, name="staff_db"),
    path('update-test/<int:test_id>/',update_test,name="update_test"),
    path('addatest',addatest,name="addatest")
]

