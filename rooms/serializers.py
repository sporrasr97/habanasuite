from rest_framework import serializers

from rooms.models import Room, House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'