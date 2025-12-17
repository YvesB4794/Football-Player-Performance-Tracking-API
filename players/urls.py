# players/urls.py
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet

router = DefaultRouter()
router.register(r'players', PlayerViewSet, basename='player')

urlpatterns = [
    path('', include(router.urls)),
    # template pages
    path('players/', views.players_list, name='players_list'),
    path('players/<int:pk>/', views.player_detail, name='player_detail'),

    # auth routes (templates in registration/)
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('accounts/register/', views.register_view, name='register'),
    path('accounts/profile/', views.profile_view, name='profile'),
]


