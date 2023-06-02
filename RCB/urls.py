from django.urls import path
from RCB.views import *
app_name="RCB"

urlpatterns=[
    path('rcb_team/',rcb_team,name='rcb_team'),
]