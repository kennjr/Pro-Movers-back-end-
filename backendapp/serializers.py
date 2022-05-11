from rest_framework import serializers

from backendapp.models import User, Request, Mover, RegUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        acc_type = validated_data['acc_type']
        if acc_type == 'mover':
            mover = Mover(
                user=user,
                name=validated_data['name']
            )
            mover.save()
        else:
            reguser = RegUser(
                user=user,
                full_name=validated_data['name']
            )
            reguser.save()
        # user.update({"acc_type": acc_type})
        return user


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"

    def create(self, validated_data):
        request = Request(
            currentLocation=validated_data['currentLocation'],
            newLocation=validated_data['newLocation'],
            user=validated_data['user'],
            mover=validated_data['mover'],
            Package=validated_data["Package"],
            packageDescription=validated_data["packageDescription"],
            movingDate=validated_data['movingDate']
        )
        request.save()
        return request


class RegUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegUser
        fields = "__all__"
        read_only_fields = ['user']


class MoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mover
        fields = '__all__'
        read_only_fields = ['user']
