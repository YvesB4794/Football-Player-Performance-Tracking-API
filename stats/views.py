# stats/views.py
from rest_framework import viewsets
from .models import PlayerStats
from .serializers import PlayerStatsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render
from .leaderboards import top_scorers

class PlayerStatsViewSet(viewsets.ModelViewSet):
    queryset = PlayerStats.objects.select_related('player','match').all()
    serializer_class = PlayerStatsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

def stats_list(request):
    stats = PlayerStats.objects.select_related('player','match').all()
    return render(request, 'stats/stats_list.html', {'stats': stats})

def leaderboard_goals(request):
    players = top_scorers()
    return render(request, 'stats/leaderboard_goals.html', {'players': players})
