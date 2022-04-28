import email
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.

class User(AbstractBaseUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True,null=True)
    bio = models.TextField(null=True)
    avatar= models.ImageField(null=True, default='avatar.svg')

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []


