from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['address', 'city', 'state', 'area', 'property_type', 'sqf', 'beds', 'baths', 'asking']