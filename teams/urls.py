from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, team_list, team_detail

router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='team')

urlpatterns = [
    path('', include(router.urls)),
    path('', team_list, name='team_list'),
    path('teams/<int:pk>/', team_detail, name='team_detail'),
]




