# matches/views.py
from rest_framework import viewsets, filters
from .models import Match
from .serializers import MatchSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render, get_object_or_404

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.select_related('home_team','away_team').all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['home_team', 'away_team', 'stadium']
    ordering_fields = ['date']

def matches_list(request):
    matches = Match.objects.select_related('home_team','away_team').all()
    return render(request, 'matches/match_list.html', {'matches': matches})

def match_detail(request, pk):
    match = get_object_or_404(Match, pk=pk)
    return render(request, 'matches/match_detail.html', {'match': match})