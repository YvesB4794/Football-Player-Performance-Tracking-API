from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Performance
from .serializers import PerformanceSerializer
from django.shortcuts import render, get_object_or_404, redirect


class PerformanceViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing player performance statistics per match.

    Provides:
    - list
    - retrieve
    - create
    - update
    - delete
    """
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering & searching
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    # Search by related fields
    search_fields = [
        'player__name',
        'match__home_team',
        'match__away_team',
    ]

    # Allow ordering results
    ordering_fields = [
        'goals',
        'assists',
        'minutes_played',
        'rating',
    ]

# -- Template views (per-app templates)
#def stat_list(request):
#    stats = Performance.objects.select_related('stats').all()
#    return render(request, 'stats/stats_list.html', {'stats': stats})

#def stat_leaderboard_goals(request):
#    stats = Performance.objects.select_related('stats').all()
#    return render(request, 'stats/leaderboard_goals.html', {'stats': stats})

def performance_list(request):
    stats = Performance.objects.select_related('stats').all()
    return render(request, 'stats/performance_list.html', {'stats': stats})

def performance_detail(request, pk):
    stat = get_object_or_404(Performance, pk=pk)
    return render(request, 'stats/performance_detail.html', {'stat': stat})