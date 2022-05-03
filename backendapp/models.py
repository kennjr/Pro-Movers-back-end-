from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=200, unique=True, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, max_length=500)
    # profile_img = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    username = models.CharField(max_length=50, null=True)
    phone = models.CharField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    is_mover = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

