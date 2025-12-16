# stats/serializers.py
from rest_framework import serializers
from .models import PlayerStats

class PlayerStatsSerializer(serializers.ModelSerializer):
    player_name = serializers.SerializerMethodField()
    match_date = serializers.SerializerMethodField()

    class Meta:
        model = PlayerStats
        fields = ['id','player','player_name','match','match_date','goals','assists','shots','passes','minutes_played','rating']

    def get_player_name(self, obj):
        return str(obj.player)

    def get_match_date(self, obj):
        return obj.match.date if obj.match else None
