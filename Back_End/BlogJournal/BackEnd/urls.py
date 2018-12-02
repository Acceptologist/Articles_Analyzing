from django.urls import path
from . import views

app_name = 'BackEnd'

urlpatterns = [
    path('CheckUser', views.CheckUser, name='CheckUser'),
    path('LogOut', views.LogOut, name='LogOut')
]
