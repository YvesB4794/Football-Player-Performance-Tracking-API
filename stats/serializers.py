from rest_framework import serializers
from .models import Performance


class PerformanceSerializer(serializers.ModelSerializer):
    player_name = serializers.StringRelatedField(source='player', read_only=True)
    match_date = serializers.DateField(source='match.date', read_only=True)

    class Meta:
        model = Performance
        fields = [
            'id',
            'player',
            'player_name',
            'match',
            'match_date',
            'goals',
            'assists',
            'shots',
            'passes',
            'minutes_played',
            'rating',
        ]
