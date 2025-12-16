# stats/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('stats/', views.stats_list, name='stats_list'),
    path('leaderboard/goals/', views.leaderboard_goals, name='leaderboard_goals'),
]
