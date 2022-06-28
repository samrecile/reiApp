from rest_framework import serializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Property
from .serializers import PropertySerializer

# Create your views here.
class caprate_list(APIView):
    def get(self, request, area=None, city=None):
        if area and city:
            properties = Property.objects.filter(city=city).order_by('-cap_rate')
            serializer = PropertySerializer(properties, many=True)
            return Response(serializer.data)
        elif city:
            properties = Property.objects.filter(city=city).order_by('-cap_rate')
            serializer = PropertySerializer(properties, many=True)
            return Response(serializer.data)
        elif area:
            properties = Property.objects.filter(area=area).order_by('-cap_rate')
            serializer = PropertySerializer(properties, many=True)
            return Response(serializer.data)
        else:
            properties = Property.objects.all().order_by('-cap_rate')
            serializer = PropertySerializer(properties, many=True)
            return Response(serializer.data)

class cashoncash_list(APIView):
    def get(self, request, area=None, city=None):
        if area and city:
            properties = Property.objects.filter(city=city).order_by('-cash_on_cash')
            serializer = PropertySerializer(properties, many=True)
            return Response(serializer.data)
        elif city:
            properties = Property.objects.filter(city=city).order_by('-cash_on_cash')
            serializer = PropertySerializer(properties, many=True)
            return Response(serializer.data)
        elif area:
            properties = Property.objects.filter(area=area).order_by('-cash_on_cash')
            serializer = PropertySerializer(properties, many=True)
            return Response(serializer.data)
        else:
            properties = Property.objects.all().order_by('-cash_on_cash')
            serializer = PropertySerializer(properties, many=True)
            return Response(serializer.data)

class price_list(APIView):
    def get(self, request, area=None, city=None):
        if area and city:
            properties = Property.objects.filter(city=city).order_by('-price')
            serializer = PropertySerializer(properties, many=True)
            return Response(serializer.data)
        elif city:
            properties = Property.objects.filter(city=city).order_by('-price')
            serializer = PropertySerializer(properties, many=True)
            return Response(serializer.data)
        elif area:
            properties = Property.objects.filter(area=area).order_by('-price')
            serializer = PropertySerializer(properties, many=True)
            return Response(serializer.data)
        else:
            properties = Property.objects.all().order_by('-price')
            serializer = PropertySerializer(properties, many=True)
            return Response(serializer.data)