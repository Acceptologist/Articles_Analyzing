from django.urls import path
from . import views

app_name = 'Articles'

urlpatterns = [
    path('', views.Articles, name='Main'),
    path('MakeArticle', views.MakeArticle, name='MakeArticle'),
    path('Article/<int:Article_id>', views.Article, name='Article'),
    path('EditArticle/<int:Article_id>', views.EditArticle, name='EditArticle')
]
