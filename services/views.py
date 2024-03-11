from django.shortcuts import render
from rest_framework import generics

from services.models import Service
from services.serializers import ServiceSerializer

# Create your views here.
class ServicesList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
class ServiceDetail(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer