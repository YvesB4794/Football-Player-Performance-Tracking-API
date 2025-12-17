from django.db import models
from players.models import Player
from matches.models import Match


class Performance(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='performances')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='performances')

    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    shots = models.PositiveIntegerField(default=0)
    passes = models.PositiveIntegerField(default=0)
    minutes_played = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

#    def __str__(self):
#        return f"{self.player.name} - {self.match}"
    def __str__(self):
        return f"{self.player} - {self.match}"

