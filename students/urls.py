from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='loginSt'),
    path('logout/', views.logout, name='logoutSt'),
    path('', views.index, name='indexSt'),
]