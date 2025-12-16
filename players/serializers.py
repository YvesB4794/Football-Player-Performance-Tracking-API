# players/serializers.py
from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name', read_only=True)
    class Meta:
        model = Player
        fields = ['id','first_name','last_name','date_of_birth','nationality','position','squad_number','team','team_name']
