from django.urls import path
from . import views

app_name = 'Services'

urlpatterns = [
    path('Help', views.Help, name='Help'),
    path('Policy', views.Policy, name='Policy'),
]
