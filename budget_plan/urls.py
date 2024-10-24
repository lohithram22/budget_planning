from django.urls import path
from . import views
urlpatterns=[
    path("",views.budget_plan,name="budget_plan")
]