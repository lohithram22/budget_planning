from django.urls import path

from . import views


urlpatterns=[
    path("",views.individual_category,name="individual_category")
]