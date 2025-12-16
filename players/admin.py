# players/admin.py
from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','team','position','squad_number')
    list_filter = ('team','position')
    search_fields = ('first_name','last_name')
