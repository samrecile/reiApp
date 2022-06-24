from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['address', 'city', 'state', 'zip_code', 'area', 'property_type', 'sqf', 'beds', 'baths', 'asking', 'cap_rate', 'cash_on_cash']