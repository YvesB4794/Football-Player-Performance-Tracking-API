# teams/views.py
from rest_framework import viewsets,filters
from .models import Team
from .serializers import TeamSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TeamViewSet(viewsets.ModelViewSet):
    """
    API: Team CRUD endpoints
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'city']
    ordering_fields = ['name']
