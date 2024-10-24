from .models import User_data
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
class CustomBackend(BaseBackend):
    def authenticate(self,request,email,password):
        try:
            user=User_data.objects.get(email=email)
            if check_password(password,user.password):
                print(user.password,user.email)
                print(email,password)
                return user
        except User_data.DoesNotExist:
            return None
