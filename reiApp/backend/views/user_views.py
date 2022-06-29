from django.http import Http404
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
 
from backend.serializers import UserSerializer, UserSerializerWithToken

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k,v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class registerUser(APIView):
    def post(self, request, format=None):
        data = request.data
        try:
            user = User.objects.create(
                first_name=data['name'],
                username=data['email'],
                email=data['email'],
                password=make_password(data['password'])
            )
            serializer = UserSerializerWithToken(user, many=False)
            return Response(serializer.data)
        except:
            message = {'detail': 'User with this email already exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class getUserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

class getUsers(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)