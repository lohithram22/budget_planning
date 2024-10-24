from django.shortcuts import render,redirect
from user.models import User_data
from django.http import HttpResponse
# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST['firstName']
        middle_name = request.POST['middleName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        phone = request.POST['phone']
        gender = request.POST['gender']
        salary = request.POST['salary']
        address = request.POST['address']
        register_user=User_data(first_name=first_name,middle_name=middle_name,last_name=last_name,email=email,password=password,phone_no=phone,gender=gender,salary=salary,address=address)
        register_user.save()
        request.session.flush()
        u_id=User_data.objects.get(email=email)
        print(u_id)
        request.session['user_data']={'user_id':u_id.user_id,'salary':u_id.salary}
        return redirect('preferences')
    else:
        return render(request,"register.html")