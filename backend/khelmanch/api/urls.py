from unicodedata import name
from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', api, name='api'),
    path("creator", CreatorView.as_view()),
    path("creator/<pk>", CreatorDetail.as_view()),
    path("sport", SportView.as_view()),
    path("sport/<int:pk>", SportDetail.as_view()),
    path("player", PlayerView.as_view()),
    path("playerfilter", PlayerViewFilter.as_view()),
    path("player/<pk>", PlayerDetail.as_view()),
    path("content", ContentView.as_view()),
    path("contentfilter", ContentViewFilter.as_view()),
    path("content/<int:pk>", ContentDetail.as_view()),
]

