from unicodedata import name
from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', api, name='api'),
    path('add-creator/', add_creator, name='add_creator'),
    path('get-creator/', get_creator, name='get_creator'),
    path('add-player/', add_player, name='add_player'),
    path('get-player/', get_creator, name='get_player'),
    path('rate-content/', add_content, name='add_content'),
    path('add-content/', rate_content, name='rate_content')
]
