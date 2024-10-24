from django.urls import path
from . import views
urlpatterns=[
    path('',views.preferences,name="preferences"),
    path('preferences_list',views.preference_list,name="preferences_list"),
]