from django.shortcuts import render, redirect
from rest_framework import viewsets

from .models import Appointments, User, Pet, Health, Daily, Appointments
from main_app import serializers
from .serializers import UserSerializer, PetSerializer, HealthSerializer, DailySerializer, AppointmentsSerializer

# Add the following import
from django.http import HttpResponse




# Define the home view
def home(request):
  return HttpResponse('<h1> (╯°□°）╯︵ ┻━┻ </h1>')

class UserView(viewsets.ModelViewSet):
  serializer_class= UserSerializer
  queryset = User.objects.all()

class PetView(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()

class HealthView(viewsets.ModelViewSet):
    serializer_class = HealthSerializer
    queryset = Health.objects.all()

class DailyView(viewsets.ModelViewSet):
    serializer_class = DailySerializer
    queryset = Daily.objects.all()

class AppointmentsView(viewsets.ModelViewSet):
    serializer_class = AppointmentsSerializer
    queryset = Appointments.objects.all()



