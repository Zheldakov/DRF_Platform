from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer

from users.validators import PasswordValidator
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'is_active']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8, max_length=16)

    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        validators = [PasswordValidator(password='password')]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(self.password)  # шифровка пороля
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    model = User
    fields = ['email', 'first_name', 'last_name', 'password', 'phone', 'is_active']
    validators = [PasswordValidator(password='password')]


class UserToTokenObtainPairSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email']=user.email
        return token

