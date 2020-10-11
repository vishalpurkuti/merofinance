from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('login/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('register/', views.register, name='signup'),
    path('', views.account, name='account'),
]
