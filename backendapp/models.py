import email
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from psycopg2 import Timestamp
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class User(AbstractBaseUser):
    full_name = models.CharField(max_length=200,unique=True,null=True)
    email = models.EmailField(unique=True,null=True)
    bio = models.TextField(null=True,max_length=500)
    profile_img = models.ImageField(null=True, default='avatar.svg')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    username = models.CharField(max_length=50,null=True)
    phone = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=100,null=True, blank=True)
    is_mover = models.BooleanField(default=False)



    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []

class Email_msg(models.Model):
    email_key = models.IntegerField(null=True)
    to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sendingTo')
    from1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receivingFrom')
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.email_msg} Email_msg'
    


class Move(models.Model):
    mover = models.ForeignKey(User, on_delete=models.CASCADE, related_name='move')
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='Move')
    scheduled_date = models.DateField((u"Conversation Date"),auto_now_add=True, blank=True)
    created_at = models.DateField((u"Conversation Date"),auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Move'

    @receiver(post_save, sender=User)
    def create_user_move(sender, instance, created, **kwargs):
        if created:
            Move.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_move(sender, instance, **kwargs):
        instance.move.save()

    def save_move(self):
        self.user

    def delete_move(self):
        self.delete()

    @classmethod
    def search_move(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

class Rating(models.Model):
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    punctuality = models.BooleanField(default=False)
    clumsy = models.BooleanField(default=False)
    experience = models.IntegerField(null=True)
    image = models.ImageField(upload_to='images/')
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return str(self.pk)






