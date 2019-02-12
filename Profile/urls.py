from django.urls import path
from . import views

app_name = 'Profile'

urlpatterns = [
    path('Settings', views.Settings, name='Settings'),
    path('Settings/<slug:Section>', views.Settings, name='Settings'),

    path('MyProfile', views.MyProfile, name='MyProfile'),
    path('MyNotifications', views.MyNotifications, name='MyNotifications'),

    path('User/<int:User_id>', views.UserProfile, name='UserProfile')
]
