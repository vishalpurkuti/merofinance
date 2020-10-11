from django.urls import path
from . import views

urlpatterns = [
    path('add-category', views.addIncomeCategory, name='addIncomeCategory')
]
