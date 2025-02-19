from django.shortcuts import render
from user.models import User_data,Preferences
# Create your views here.
import json
def individual_category(request):
    if request.method=="POST":
        category=request.POST.get("category")
        user_data=request.session.get("user_data",{})
        u_id = user_data["user_id"]
        user=User_data.objects.get(user_id=u_id)
        print(user.first_name)
        preference=Preferences.objects.get(user_id=user,Category=category)
        data_list=[preference.amount,preference.expenses]
        print(data_list)
        label=["Amount","Expenses"]

        print("avuthaadi le no worries ",category)
        context = {
            'data': json.dumps(data_list),
            'label':json.dumps(label)
        }
        return render(request,"individual_category.html",context)

