from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
# https://api-promovers.herokuapp.com/
# usertwo@users.com token: aa25ca8f13c18c5ef66607558c4554ee3ec8813f

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, Request
from .serializers import UserSerializer, RequestSerializer

from django.conf import settings
from django.core.mail import send_mail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['email'] = user.email
        token['username'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    data = {}
    if serializer.is_valid(raise_exception=True):
        acc_type = request.data['acc_type']
        instance = serializer.create(validated_data=request.data)

        if instance:
            # token = Token.objects.get(user=instance).key
            # The email section
            subject = 'Welcome to ProMovers'
            if acc_type == "mover":
                message = f"Hi {instance.username}, thank you for registering in as a mover on ProMovers. Where we will connect you to potential clients. Here's your authentication token {token}"
            else:
                message = f"Hi {instance.username}, thank you for registering in as a user on ProMovers. Here's your authentication token {token}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [instance.email, ]
            send_mail(subject, message, email_from, recipient_list)

            # data['token'] = token
            data['user_id'] = instance.id
            data['response'] = "User registration, successful"
        else:
            data['response'] = "User registration, failed"
        return Response(data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def api_get_all_users(request):
    users = User.objects.filter(acc_type="user").all()

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def api_specific_user(request, uid):
    try:
        users = User.objects.get(id=uid)
        serializer = UserSerializer(users, many=False)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response({"response": "404"}, status=404)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def new_move_request(request):
    serializer = RequestSerializer(data=request.data)
    data = {}
    if serializer.is_valid(raise_exception=True):
        instance = serializer.create(validated_data=request.data)

        if instance:

            # The email section
            # subject = 'New move request'
            #
            # message = f"Your move request from {instance.from_location} to {instance.to_location} has been made successfully. \nExpect a response from the mover"
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [instance.email, ]
            # send_mail(subject, message, email_from, recipient_list)

            data['response'] = "Request made successfully"
            return Response(data, status=200)
        else:
            data['response'] = "User registration, failed"
            return Response(data, status=400)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def api_get_all_users_requests(request, uid):
    users = Request.objects.filter(user_id=uid).all()

    serializer = RequestSerializer(users, many=True)
    return Response(serializer.data)

