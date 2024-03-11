from rest_framework import serializers

from rooms.models import Room, House
from services.serializers import ServiceSerializer
        
class RoomSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['id', 'name', 'description', 'images', 'services']
        
class HouseSerializer(serializers.ModelSerializer):
    get_house_rooms = RoomSerializer(many=True, read_only=True)
    class Meta:
        model = House
        fields = ['id', 'name', 'about', 'email', 'address', 'images', 'get_house_rooms']