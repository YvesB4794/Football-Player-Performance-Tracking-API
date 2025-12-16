# stats/models.py
from django.db import models
from players.models import Player
from matches.models import Match

class PlayerStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='stats')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='player_stats')
    goals = models.PositiveSmallIntegerField(default=0)
    assists = models.PositiveSmallIntegerField(default=0)
    shots = models.PositiveSmallIntegerField(default=0)
    passes = models.PositiveIntegerField(default=0)
    minutes_played = models.PositiveSmallIntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('player', 'match')
        ordering = ['-match__date']

    def __str__(self):
        return f"{self.player} — {self.match}"
