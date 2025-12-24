from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerformanceViewSet, performance_list, performance_detail
from . import views


router = DefaultRouter()
router.register(r'stats', PerformanceViewSet, basename='stat')

urlpatterns = [
    path('', include(router.urls)),
    # template pages
    path('', performance_list, name='performance_list'),
    path('stats/', views.performance_detail, name='performance_detail'),
]


#    path('stats/', views.stat_list, name='stat_list'),
#    path('stats/<int:pk>/', views.stat_list, name='stat_list'),
#    path('stats/', views.stat_leaderboard_goals, name='stat_leaderboard_goals'),
#    path('stats/<int:pk>/', views.stat_leaderboard_goals, name='stat_leaderboard_goals'),

