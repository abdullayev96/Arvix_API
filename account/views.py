from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import status
from .utils import *
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import *
from django.http import JsonResponse

from rest_framework.generics import GenericAPIView

from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie

from django.conf import settings
from django.contrib.auth import authenticate
from django.middleware import csrf

from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


#
# class RegisterAPI(APIView):
#     def post(self, request):
#         try:
#             data=request.data
#             serializer  = RegisterSerializer(data=data)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 send_otp_email(serializer.data['email'])
#                 return Response({"data":status.HTTP_201_CREATED})
#
#         except Exception as e:
#             print(e)
#
#         return Response({"status":status.HTTP_400_BAD_REQUEST})

class RegisterAPI(GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, format=None):
        try:
            serializer = self.get_serializer(data=request.data, many=False)
            if serializer.is_valid():
                 serializer.save()
                 send_otp_email(serializer.data['email'])
                 return Response({"status":status.HTTP_201_CREATED})
            return Response({"status":status.HTTP_404_NOT_FOUND})

        except Exception as e:
                  print(e)

        return Response({"status": status.HTTP_400_BAD_REQUEST})



class VerifyOTPAPI(APIView):
    def post(self, request):
        try:
            data=request.data
            serializer = VerifySerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                email = serializer.data['email']
                otp = serializer.data['otp']

                user = CustomUser.objects.filter(email=email)
                if not user.exists():
                    return Response({"status": status.HTTP_400_BAD_REQUEST,
                                     "message": "Try again IT is wrong ",
                                     "data": "Invalid OTP or email"})

                if not user[0].otp != otp:
                    return Response({"status": status.HTTP_400_BAD_REQUEST,
                                     "message": "Try again It is wrong ",
                                     "data": "wrong  OTP "})

                user = user.first()
                user.staff = True
                user.save()

                return Response({"status": status.HTTP_200_OK,
                                 "message": "Your account activate",
                                 "data": serializer.data})

            return Response({"status": status.HTTP_404_NOT_FOUND})

        except Exception as e:
            print(e)


