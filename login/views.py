from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth
from django.http import HttpResponse
from user.models import User_data
from home import views
# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)

        user=User_data.objects.get(email=email)
        print(type(user.password))
        print(type(password))
        if password==user.password:
            user.is_active=True
            user.save()
            request.session['user_data']={'name':user.first_name,'is_active':True,'user_id':user.user_id}
            return redirect('root')
        else:
            return HttpResponse("Idi avvatledd kani aapesi thongo evng chuuddam ")
    else:
         return render(request,"login.html")
