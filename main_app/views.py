from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from models import User

# Add the following import
from django.http import HttpResponse

#import models
from .models import User


# Define the home view
def home(request):
  return HttpResponse('<h1> (╯°□°）╯︵ ┻━┻ </h1>')

class UserView(viewsets.ModelViewSet):
  serializer_class= UserSerializer
  queryset = User.objects.all()



