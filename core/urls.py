"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# core/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from teams.views import TeamViewSet
from players.views import PlayerViewSet
from matches.views import MatchViewSet
from stats.views import PerformanceViewSet

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'player-stats', PerformanceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/players/', include('players.urls')),
    path('api/v1/teams/', include('teams.urls')),
    path('api/v1/matches/', include('matches.urls')),
    path('api/v1/stats/', include('stats.urls')),
]
