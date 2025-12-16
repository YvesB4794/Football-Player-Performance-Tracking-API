# stats/admin.py
from django.contrib import admin
from .models import PlayerStats

@admin.register(PlayerStats)
class PlayerStatsAdmin(admin.ModelAdmin):
    list_display = ('player','match','goals','assists','minutes_played')
    list_filter = ('match', 'player')
    search_fields = ('player__first_name','player__last_name')
