from django.urls import path
from . import views

app_name = 'Register'

urlpatterns = [
    path('SignUP', views.SignUP, name='SignUP'),
    path('Login', views.Login, name='Login'),
]
