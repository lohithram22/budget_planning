from django.shortcuts import render

# Create your views here.
def home(request):
    user_data=request.session.get('user_data',{})
    if user_data =={}:
        return render(request,"home.html", {"is_login":False})
    else:
        return render(request,"home.html",{'user_data':user_data,"is_login":True})

