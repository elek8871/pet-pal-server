
from django.urls import path, include
from . import views
from rest_framework import routers
from user import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.User, name='user')
]

