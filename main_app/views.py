from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

#import models
from .models import User


# Define the home view
def home(request):
  return HttpResponse('<h1> (╯°□°）╯︵ ┻━┻ </h1>')



