# matches/admin.py
from django.contrib import admin
from .models import Match

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('home_team','away_team','date','home_score','away_score')
    list_filter = ('competition',)
    search_fields = ('home_team__name','away_team__name')
