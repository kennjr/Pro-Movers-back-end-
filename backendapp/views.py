from django.core.exceptions import ObjectDoesNotExist
# https://api-promovers.herokuapp.com/
# usertwo@users.com token: aa25ca8f13c18c5ef66607558c4554ee3ec8813f

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, Request, RegUser, Mover
from .serializers import UserSerializer, RequestSerializer, RegUserSerializer, MoverSerializer

from django.conf import settings
from django.core.mail import send_mail
import coreapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


# This class is for the documentation of the api
class ProMoversApiSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ["put", "post"]:
            extra_fields = [
                coreapi.Field(name="bio", required=False)
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


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
                message = f"Hi {instance.username}, thank you for registering in as a mover on ProMovers. Where we will connect you to potential clients."
            else:
                message = f"Hi {instance.username}, thank you for registering in as a user on ProMovers."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [instance.email, ]
            send_mail(subject, message, email_from, recipient_list)

            # data['token'] = token
            data['user_id'] = instance.id
            data['response'] = "User registration, successful"

            return Response(data, status=200)
        else:
            data['response'] = "User registration, failed"
            return Response(data, status=400)


@api_view(['PUT'])
def api_update_user_profile(request, username):
    user_id = request.data['user']
    user = RegUser.get_user_by_username(username)
    if user:
        serializer = RegUserSerializer(user, request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {"message": "Update was successful", "user": user_id}
            return Response(data, status=200)
    else:
        data = {"message": "User doesn't exist"}
        return Response(data, status=404)


@api_view(['PUT'])
def api_update_mover_profile(request, username):
    user_id = request.data['user']
    mover = Mover.get_mover_by_username(username)
    if mover:
        data = request.data.pop("user")
        serializer = MoverSerializer(mover, data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {"message": "Update was successful"}
            return Response(data, status=200)
    else:
        data = {"message": "Mover doesn't exist", "user": user_id}
        return Response(data, status=404)


@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def api_get_all_users(request):
    users = RegUser.objects.all()
    serializer = RegUserSerializer(users, many=True)
    # try:
    #     print(f"The current user is {request.user}")
    # except:
    #     print("The except clause ran")
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def api_get_all_movers(request):
    movers = Mover.objects.all()
    serializer = MoverSerializer(movers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def api_get_specific_user(request, username):
    try:
        users = RegUser.objects.get(user__username=username)
        serializer = RegUserSerializer(users, many=False)
        return Response(serializer.data, status=200)
    except ObjectDoesNotExist:
        return Response({"response": "404"}, status=404)


@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def api_get_specific_mover(request, username):
    try:
        users = Mover.objects.get(user__username=username)
        serializer = RegUserSerializer(users, many=False)
        return Response(serializer.data, status=200)
    except ObjectDoesNotExist:
        return Response({"response": "404"}, status=404)


@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def new_move_request(request):
    serializer = RequestSerializer(data=request.data)
    data = {}
    if serializer.is_valid(raise_exception=True):
        instance = serializer.create(validated_data=request.data)

        if instance:
            data['response'] = "Request created successfully"
            return Response(data, status=200)
        else:
            data['response'] = "User registration, failed"
            return Response(data, status=400)


@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def api_get_all_users_requests(request, username):
    users = Request.objects.filter(user__username=username).all()

    serializer = RequestSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def api_get_all_requests(request):
    users = Request.objects.all()

    serializer = RequestSerializer(users, many=True)
    return Response(serializer.data)

