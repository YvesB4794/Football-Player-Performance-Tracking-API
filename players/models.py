# players/models.py
from django.db import models
from teams.models import Team
from django.contrib.auth.models import User

class Player(models.Model):
    POSITIONS = [
        ('GK', 'Goalkeeper'),
        ('DF', 'Defender'),
        ('MF', 'Midfielder'),
        ('FW', 'Forward'),
    ]

    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='players')
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=80, blank=True, null=True)
    position = models.CharField(max_length=2, choices=POSITIONS)
    squad_number = models.PositiveSmallIntegerField(blank=True, null=True)

    # optional link to a Django User if needed (comment out if not using)
    # user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
