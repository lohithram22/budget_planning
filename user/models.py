from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User_data(AbstractUser):
    user_id=models.AutoField(primary_key=True,)
    first_name=models.CharField(max_length=30)
    middle_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    phone_no=models.BigIntegerField()
    gender=models.CharField(max_length=10)
    salary=models.IntegerField()
    address=models.CharField(max_length=50)
class Preferences(models.Model):
    user_id=models.ForeignKey(User_data,on_delete=models.CASCADE)
    pref_no=models.IntegerField()
    Category=models.CharField()
    weightage=models.PositiveIntegerField()
    amount=models.PositiveIntegerField()
    is_constant=models.BooleanField(default=False)
    expenses=models.PositiveIntegerField(default=0)








