from django.shortcuts import render,redirect
import json
from django.http import HttpResponse
from user.models import Preferences
from user.models import User_data
# Create your views here.
def preferences(request):
    if request.method=="POST":

        pref1=request.POST['preference 1']
        pref2=request.POST['preference 2']
        pref3=request.POST['preference 3']
        pref4=request.POST['preference 4']
        pref5=request.POST['preference 5']
        pref6=request.POST['preference 6']
        pref7=request.POST['preference 7']
        pref8=request.POST['preference 8']
        pref9=request.POST['preference 9']
        pref10=request.POST['preference 10']
        pref11=request.POST['preference 11']
        pref12=request.POST['preference 12']
        pref13=request.POST['preference 13']
        preferences=[pref1,pref2,pref3,pref4,pref5,pref6,pref7,pref8,pref9,pref10,pref11,pref12,pref13]
        data=request.session.get('user_data',{})
        print(data)
        u_id=data["user_id"]
        salary=data["salary"]
        pref_no=0
        total_amount=0
        total_weight=0
        user_instance=User_data.objects.get(user_id=u_id)
        for pref in preferences:
            pref_no=pref_no+1
            if pref_no<=3:
                weight=12
                total_weight+=weight
                amount=(salary*weight)/100
                total_amount+=amount
            elif pref_no>3 and pref_no<7:
                weight=9
                total_weight+=weight
                amount=(salary*weight)/100
                total_amount+=amount

            elif pref_no>6 and pref_no<10:
                weight=7
                total_weight+=weight
                amount=(salary*weight)/100
                total_amount+=amount

            elif pref_no>9 and pref_no<=12:
                weight=5
                total_weight+=weight
                amount=(salary*weight)/100
                total_amount+=amount

            else:
                if total_amount<salary:
                    amount=salary-total_amount
                    weight=100-total_weight
                elif total_amount==salary:
                    amount=0
                    weight=0
            preferences=Preferences(pref_no=pref_no,Category=pref,weightage=weight,user_id=user_instance,amount=amount)
            preferences.save()
            #request.session.flush()


        #for pref in values:
        return redirect("preferences_list")
    else:
        return render(request,'preferences.html')
def preference_list(request):
    data = request.session.get('user_data', {})
    print(data)
    u_id = data["user_id"]
    user_instance = User_data.objects.get(user_id=u_id)
    name=user_instance.first_name
    preferences = Preferences.objects.filter(user_id=user_instance)

    return render(request,'preferences_list.html',{'preferences':preferences,'name':name})
