from django.shortcuts import render
from user.models import Preferences,User_data
# Create your views here.
import json
def visualise(request):

        user_data = request.session.get("user_data", {})
        u_id = user_data["user_id"]
        user = User_data.objects.get(user_id=u_id)
        preferences = Preferences.objects.filter(user_id=user).order_by("pref_no")
        categories = [pref.Category for pref in preferences]
        weights = [pref.weightage for pref in preferences]
        amount = [pref.amount for pref in preferences]
        context = {
            'categories': json.dumps(categories),
            'amounts': json.dumps(amount),
        }
        return render(request, 'visualisation.html', context)

# {"categories":categories,"amount":amount}