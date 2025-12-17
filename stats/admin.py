from django.contrib import admin
from .models import Performance


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = (
        'player',
        'match',
        'goals',
        'assists',
        'shots',
        'passes',
        'minutes_played',
        'rating',
    )

    list_filter = (
        'match',
        'player',
    )

    search_fields = (
        'player__first_name',
        'player__last_name',
    )

    ordering = (
        '-match__date',
        '-rating',
    )
