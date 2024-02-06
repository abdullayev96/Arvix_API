from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from rest_framework.serializers import Serializer
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth.hashers import make_password




class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=70, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['full_name','middle_name','number','email',
                  'username', 'password', 'is_staff']


    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class VerifySerializer(serializers.Serializer):
     email  = serializers.EmailField()
     otp  = serializers.CharField()

     class Meta:
          model = CustomUser
          fields = ['email', 'otp']



class LoginSerializer(serializers.ModelSerializer):
     email = serializers.EmailField()
     password  = serializers.CharField()


     class Meta:
          model  = CustomUser
          fields = ['email', 'password']

# class LoginSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()
#     tokens = serializers.SerializerMethodField()
#
#
#     def get_tokens(self, obj):
#         user = CustomUser.objects.get(email=obj['email'])
#         return {
#             'refresh': user.tokens()['refresh'],
#             'access': user.tokens()['access']}
#
#     class Meta:
#         model = CustomUser
#         fields = ['email','password','tokens']
#
#     def validate(self, attrs):
#         email = attrs.get('email','')
#         password = attrs.get('password','')
#         user = auth.authenticate(email=email,password=password)
#         if not user:
#             raise AuthenticationFailed('Invalid credentials, try again')
#         if not user.is_active:
#             raise AuthenticationFailed('Account disabled, contact admin')
#         return {
#             'email': user.email,
#             'tokens': user.tokens
#         }
#
