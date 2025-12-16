# stats/leaderboards.py
from django.db.models import Sum
from players.models import Player

def top_scorers(limit=10):
    """
    Returns Player queryset annotated with total_goals.
    """
    qs = Player.objects.annotate(total_goals=Sum('stats__goals')).order_by('-total_goals')[:limit]
    return qs
