import email
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.

class User(AbstractBaseUser):
    full_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True,null=True)
    bio = models.TextField(null=True)
    profile_img = models.ImageField(null=True, default='avatar.svg')
    created_at=models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    phone = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=100)
    is_mover = models.BooleanField(default=False)



    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []


