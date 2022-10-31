from django.contrib import admin
from .models import Appointments, Daily, User, Health, Pet

# Register your models here
admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Health)
admin.site.register(Daily)
admin.site.register(Appointments)

