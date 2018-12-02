from django.urls import path
from . import views

app_name = 'Blogs'

urlpatterns = [
    path('', views.Main, name='Main'),
    path('Make_Blog', views.MakeBlog, name='MakeBlog')
]
