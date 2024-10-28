from faker import Faker
from django.contrib.auth.models import User
from .models import *
fake= Faker()

def seed_db(n=10)->None:
  for i in range(0,n):
    first_name= fake.first_name()
    last_name= fake.first_name()
    username= first_name.lower() + last_name.lower()
    mobile_number= fake.bothify(text='##########')
    if User.objects.filter(username= username).exists() or UserInfo.objects.filter(mobile_number= int(mobile_number)).exists():
      continue
    email= username + "@gmail.com"
    password= "123456789"

    user=User.objects.create(
      username= username,
      first_name= first_name,
      last_name= last_name,
      email= email,
    )
    user.set_password(password)
    user.save()

    userinfo= UserInfo.objects.create(
      user= user,
      mobile_number= mobile_number,
    )
    userinfo.save()