from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Property

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = 'Hello'
        return name

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['address', 'city', 'state', 'zip_code', 'area', 'property_type', 'sqf', 'beds', 'baths', 'asking', 'cap_rate', 'cash_on_cash']

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']
    
    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token)
