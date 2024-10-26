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
        if preferences.is_constant == True:
            return redirect("root")
        salary=user.salary
        if not weightage and amount:

            old_amt=preferences.amount
            new_amt=amount
            if old_amt<new_amt:
                need_amt=new_amt-old_amt
                print("idi kaavalasina amount ra",need_amt)
                pref_no=13
                total=0
                while(preferences.is_constant !=True):
                    if pref_no==0:
                        pref_no=13
                    pref=Preferences.objects.get(user_id=user,pref_no=pref_no)
                    if pref.Category==category:
                        pref_no-=1
                    if pref.amount<=need_amt:
                        pref_no=pref_no-1
                    elif pref.is_constant ==True:
                        pref_no=pref_no-1
                    elif pref.amount>need_amt:
                        contrib=int(need_amt/10)
                        pref.amount=pref.amount-contrib
                        print(contrib, " taken from the category ", pref.Category)
                        total+=contrib
                        pref.save()
                        if total==need_amt:
                            preferences.amount+=total
                            preferences.save()
                            break
                        else:
                            pref_no-=1
                            continue
            elif old_amt>new_amt:
                need_amt=old_amt-new_amt
                left=0
                if need_amt%10 != 0:
                    left = need_amt % 10
                    need_amt = need_amt - left
                    print("Idi kaavalasina amount ra babu ", need_amt,"idi left over ra",left)
                pref_no=1
                total = 0
                while (preferences.is_constant !=True):
                    if pref_no == 14:
                        pref_no = 1
                    pref = Preferences.objects.get(user_id=user, pref_no=pref_no)
                    if pref.Category==category:
                        pref_no+=1
                    if pref.is_constant == True:
                        pref_no = pref_no + 1
                    else:

                        if pref_no==13:
                            pref.amount=pref.amount-left
                            pref.save()
                            total+=left
                            print("aaaa left add chessan chuud total ki ",left,"idi left add chesaka amount uu",pref.amount)
                        contrib = int(need_amt / 10)
                        pref.amount = pref.amount + contrib
                        print(contrib, " added to the category ", pref.Category)
                        total += contrib
                        pref.save()
                        if total == need_amt:
                            preferences.amount -= total

                            preferences.save()
                            break
                        else:
                            pref_no += 1
                            continue



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
        if is_constant:
            preferences.is_constant = True
            preferences.save()
        else:
            preferences.is_constant = False
            preferences.save()
        return redirect("root")

    return render(request,'customize.html')