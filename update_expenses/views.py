from django.shortcuts import render,redirect
from user.models import User_data,Preferences
# Create your views here.
def update(request):
    if request.method=="POST":
        category=request.POST.get("preference")
        amount=int(request.POST.get("spent"))
        print("This see ra gorri",amount,category)
        data = request.session.get('user_data', {})
        u_id = data["user_id"]
        print("idi kuda chudu ra ",u_id)
        user=User_data.objects.get(user_id=u_id)
        preferences=Preferences.objects.get(user_id=user,Category=category)
        print(preferences.amount,"idi okka sari chusko ")
        expense=int(preferences.expenses)
        if expense is None:
            preferences.expenses=amount
            preferences.save()
        else:
            preferences.expenses=expense+amount
            preferences.save()
        return redirect("root")
    else:
        return render(request,"update_expenses.html")