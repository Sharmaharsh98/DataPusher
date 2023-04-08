from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

# Create your models here.
class User_Account(AbstractBaseUser, PermissionsMixin):
    account_id = models.IntegerField(null=True)
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return self.email


