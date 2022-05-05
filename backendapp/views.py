from django.shortcuts import render
# https://api-promovers.herokuapp.com/
# usertwo@users.com token: aa25ca8f13c18c5ef66607558c4554ee3ec8813f

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer

from django.conf import settings
from django.core.mail import send_mail


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    data = {}
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()

        if instance:
            token = Token.objects.get(user=instance).key
            # The email section
            subject = 'Welcome to ProMovers'
            if instance.acc_type == "mover":
                message = f"Hi {instance.username}, thank you for registering in as a mover on ProMovers. Where we will connect you to potential clients. Here's your authentication token {token}"
            else:
                message = f"Hi {instance.username}, thank you for registering in as a user on ProMovers. Here's your authentication token {token}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [instance.email, ]
            send_mail(subject, message, email_from, recipient_list)

            data['token'] = token
            data['response'] = "User registration, successful"
        else:
            data['response'] = "User registration, failed"
        return Response(data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def api_get_all_users(request):
    users = User.objects.all()

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def api_specific_user(request, uid):
    users = User.objects.get(id=uid)

    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)
