# players/views.py
from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from .forms import RegisterForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

class PlayerViewSet(viewsets.ModelViewSet):
    """
    API: Player CRUD endpoints
    """
    queryset = Player.objects.select_related('team').all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# -- Template views (per-app templates)
def players_list(request):
    players = Player.objects.select_related('team').all()
    return render(request, 'players/player_list.html', {'players': players})

def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'players/player_detail.html', {'player': player})

# -- Auth views (registration + profile)
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect('players_list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'registration/profile.html', {'form': form})
