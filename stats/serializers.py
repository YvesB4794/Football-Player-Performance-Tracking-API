from rest_framework import serializers
from .models import Performance


class PerformanceSerializer(serializers.ModelSerializer):
    player_name = serializers.StringRelatedField(source='player', read_only=True)
    #match_date = serializers.DateField(source='match.date', read_only=True)
    match_date = serializers.SerializerMethodField()

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

    def get_match_date(self, obj):
        if obj.match and obj.match.date:
            return obj.match.date.date()  # ✅ convert datetime → date
        return None