
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
# def __str__(self):
#     return self.name

class UserManager(BaseUserManager):
    def create_user(self, email, password, username, **extra_fields):

        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
        email = self.normalize_email(email),
                username = username,
                **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username, **extra_fields):
        # if password is None:
        #     raise TypeError('Superusers must have a password.')
        # if email is None:
        #     raise TypeError('Superusers must have an email.')
        # if username is None:
        #     raise TypeError('Superusers must have an username.')     

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        user = self.create_user(email, password, username, **extra_fields)
        # user.save()
        return user       


class User(AbstractBaseUser,PermissionsMixin):
    userId = models.AutoField(primary_key=True)
    email = models.EmailField(db_index=True, unique=True, max_length=250)
    username = models.CharField(unique=True, max_length=240)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) 
    breed = models.CharField(max_length=100) 
    date_of_birth = models.DateField(null=True)
    nickname = models.CharField(max_length=100) 
    catchphrase = models.CharField(max_length=250) 

    def __str__(self):
        return self.name

class Health(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=True, null=True)
    visit_date = models.DateField(null=True)
    visit_type = models.CharField(max_length=250,blank=True, null=True)
    pet_weight = models.CharField(max_length=25, blank=True, null=True)
    shots = models.CharField(max_length= 500,blank=True, null=True)
    medicine = models.CharField(max_length=500, blank=True, null=True)
    other =models.TextField(blank=True, null=True)
    tx_plan = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.notes

class Daily(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=True, null=True)
    food_schedule = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    walk_schedule = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    potty_trips = models.TimeField(auto_now =False, auto_now_add=False, blank=True, null=True)
    medicine_schedule = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.notes

class Appointments(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, blank=True, null=True)
    grooming =  models.DateField(null=True, blank=True)
    play_date =  models.DateField(null=True,blank=True)
    cuddles =  models.DateField(null=True,blank=True)
    notes =models.TextField(blank=True, null=True)

    def __str__(self):
        return self.notes