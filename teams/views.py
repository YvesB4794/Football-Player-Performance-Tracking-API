# teams/views.py
from rest_framework import viewsets
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
