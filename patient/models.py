from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
  user= models.ForeignKey(User, on_delete= models.CASCADE)
  first_name= models.CharField(max_length= 255)
  last_name= models.CharField(max_length= 255, blank= True, null= True)
  dob= models.DateField(default= None)
  sex= models.CharField(max_length= 10, choices= [('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], default= 'FEMALE')

  def __str__(self) -> str:
    return self.first_name