from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    data = {}
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        if instance:
            token = Token.objects.get(user=instance).key
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
