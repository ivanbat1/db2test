from . import views
from django.urls import path, include

urlpatterns = [
    path('login/', views.logowanie),
    path('logout/', views.logout),
    path('register/', views.register),
    path('activate/<slug:uidb64>/<slug:token>)/', views.activate, name='activate'),
]