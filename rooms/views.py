from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework import generics

from rooms.models import Room, House
from rooms.serializers import HouseSerializer

# Create your views here.
class RoomListView(ListView):
    model = Room

class HouseDetailView(generics.RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer