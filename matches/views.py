# matches/views.py
from rest_framework import viewsets
from .models import Match
from .serializers import MatchSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.select_related('home_team','away_team').all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

def matches_list(request):
    matches = Match.objects.select_related('home_team','away_team').all()
    return render(request, 'matches/match_list.html', {'matches': matches})
