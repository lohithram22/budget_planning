from django.shortcuts import render
from user.models import User_data,Preferences
# Create your views here.
def budget_plan(request):
    data = request.session.get('user_data', {})
    print(data)
    u_id = data["user_id"]
    user=User_data.objects.get(user_id=u_id)
    preferences=Preferences.objects.filter(user_id=user)
    return render(request,"budget_plan.html",{'preferences':preferences})
