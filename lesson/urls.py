from . import views
from django.urls import path, include

urlpatterns = [
    path('articles/all/', views.articles),
    path('article/get/<int:article_id>/', views.article),
    path('article/addlike/<int:article_id>/', views.addlike),
    path('article/addcomment/<int:article_id>/', views.addcomment),
    path('', views.articles),
]