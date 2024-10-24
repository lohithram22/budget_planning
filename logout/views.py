from django.shortcuts import render,redirect
from user.models import User_data
# Create your views here.
def logout(request):
    request.session.flush()
    return redirect('home')