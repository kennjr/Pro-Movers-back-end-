from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import BaseUserManager, PermissionsMixin


# Create your models here.
# https://app.getpostman.com/join-team?invite_code=f7cb4d2aa2b3e7e6587102b6766518f9


class MyMgr(BaseUserManager):

    def create_user(self, email, username, password=None):
        user = self.model(
            email=username,
            username=email,
            password=password
        )
        user.is_admin = False
        user.is_staff = False
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            username,
            email,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email_):
        return self.get(email=email_)

    def __str__(self):
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        # "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # "Does the user have permissions to view the app 'app_label'?"
        return True


class User(AbstractBaseUser, PermissionsMixin):
    objects = MyMgr()

    full_name = models.CharField(max_length=200, unique=False, null=True, blank=True)
    email = models.EmailField(verbose_name='email', unique=True, null=False, db_index=True)
    bio = models.TextField(null=True, max_length=500)
    # profile_img = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    username = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(null=True, blank=True, max_length=22)
    location = models.CharField(max_length=100, null=True, blank=True)
    acc_type = models.CharField(max_length=7, default="user", null=False, blank=False)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Request(models.Model):
    from_location = models.CharField(max_length=99, blank=False, null=False)

