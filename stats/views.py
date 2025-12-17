from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Performance
from .serializers import PerformanceSerializer


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
