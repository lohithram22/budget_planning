from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.models import User_data,Preferences
# Create your views here.
def customize(request):
    if request.method=="POST":
        category=request.POST.get("preference")
        amount=request.POST.get("amount")
        weightage=request.POST.get("weightage")
        is_constant=request.POST.get("is_constant")
        if weightage:
            weightage=int(weightage)
        elif amount:
            amount=int(amount)
        if is_constant=="no":
            is_constant=False
        else:
            is_constant=True

        print(category,amount,weightage,is_constant)
        data=request.session.get('user_data',{})
        u_id=data["user_id"]
        print(u_id)
        user=User_data.objects.get(user_id=u_id)
        preferences=Preferences.objects.get(Category=category,user_id=user)
        if not weightage and amount:
            old_amt=preferences.amount
            print(old_amt)
            if old_amt<amount:

                need_amt=amount-old_amt
                pref_no=13
                collected=0
                while(True):
                    pref1=Preferences.objects.get(user_id=user,pref_no=13)
                    if pref1.is_constant !=False:
                        pref_no-=1
                    elif pref1.amount<=amount:
                        pref_no-=1
                    elif pref1.amount>amount:
                        contrib=need_amt/10
                        pref1.amount-=contrib
                        collected+=contrib
                        need_amt=need_amt-contrib
                        pref_no=pref_no-1
                        if pref_no==0:
                            pref_no=13
                        if is_constant:
                            preferences.is_constant = True
                        else:
                            preferences.is_constant = False
                        pref1.save()
                        preferences.save()
                        if need_amt!=0:
                            continue
                        else:
                            break
                preferences.amount += collected





            else:
                pass

        elif not amount and weightage:
            old_weight=preferences.weightage
            if old_weight<weightage:
                need_weight=weightage-old_weight
                pref_no=13
                while(True):
                    pref=Preferences.objects.get(user_id=user,pref_no=pref_no)
                    if pref.weightage<=need_weight:
                        pref_no=pref_no-1
                    elif pref.is_constant != False:
                        pref_no=pref_no-1
                    else:
                        pref.weightage=pref.weightage-1
                        need_weight-=1
                        preferences.weightage=preferences.weightage+1
                        pref_no-=1
                        if is_constant:
                            preferences.is_constant=True
                        else:
                            preferences.is_constant=False
                        pref.save()
                        preferences.save()
                        if need_weight!=0:
                            continue
                        else:
                            break

            elif old_weight>weightage:
                excess_weight=old_weight-weightage
                pref_no=1
                while(True):
                    pref = Preferences.objects.get(user_id=user, pref_no=pref_no)
                    if pref.is_constant != False:
                        pref_no=pref_no+1
                    else:
                        pref.weightage=pref.weightage+1
                        excess_weight-=1
                        preferences.weightage = preferences.weightage -1
                        pref_no+=1
                        if is_constant:
                            preferences.is_constant=True
                        else:
                            preferences.is_constant=False
                        pref.save()
                        preferences.save()
                        if excess_weight != 0:
                            continue
                        else:
                            break

        print(preferences.pref_no)
        return redirect("root")

    return render(request,'customize.html')