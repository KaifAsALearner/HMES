from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Staff(models.Model):
  user= models.OneToOneField(User, on_delete= models.CASCADE)
  dob= models.DateField(default= None)
  sex= models.CharField(max_length= 10, choices= [('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], default= 'FEMALE')