from django.urls import path
from . import views

app_name = 'BackEnd'

urlpatterns = [
    path('CheckName', views.CheckName, name='CheckName'),
    path('CheckEmail', views.CheckEmail, name='CheckEmail'),

    path('LogOut', views.LogOut, name='LogOut'),

    path('GetPosts', views.GetPosts, name='GetPosts'),

    path('MakeComment', views.MakeComment, name='MakeComment'),
    path('LikeDisLikePost', views.Like_DisLikePost, name='Like_DisLikePost'),

    path('DeletePost', views.DeletePost, name='DeletePost'),

    path('GetNotifications', views.GetMoreNotifications, name='GetNotifications')
]
