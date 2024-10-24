from django.shortcuts import render

# Create your views here.
def root(request):
    user_data=request.session.get('user_data',{})
    name=user_data["name"]
    return render(request,'root.html',{'name':name})