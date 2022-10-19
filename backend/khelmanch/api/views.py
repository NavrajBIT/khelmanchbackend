from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    CreatorSerializers, PlayerSerializers, SportSerializers, ContentSerilizers
)
from .models import Content, Creator, Player, Sport
from django.http import JsonResponse
from rest_framework import generics

from .contractcalls import test_contract

class CreatorView(generics.ListCreateAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializers
   


class CreatorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializers

#############################################
class SportView(generics.ListCreateAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializers
    def post(self, request, *args, **kwargs):
        print(request.method)
        test_contract()
        return self.create(request, *args, **kwargs)


class SportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializers
    def put(self, request, *args, **kwargs):
        print(request.method)
        test_contract()
        return self.update(request, *args, **kwargs)

#############################################
class PlayerView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializers

class PlayerViewFilter(generics.ListAPIView):
    serializer_class = PlayerSerializers
    def get_queryset(self):       
        profileCreator = self.request.query_params.get('profileCreator')      
        return Player.objects.filter(profileCreator=profileCreator)


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializers

##############################################
class ContentView(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerilizers

class ContentViewFilter(generics.ListAPIView):
    serializer_class = ContentSerilizers
    def get_queryset(self):       
        contentCreator = self.request.query_params.get('contentCreator')      
        return Content.objects.filter(contentCreator=contentCreator)

class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerilizers



