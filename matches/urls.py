# matches/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('matches/', views.matches_list, name='matches_list'),
]
