from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    CreatorSerializers, PlayerSerializers, SportSerializers, ContentSerilizers, UserSerilizers, CommentSerilizers
)
from .models import Content, Creator, Player, Sport, User, Comment
from django.http import JsonResponse
from rest_framework import generics

from .contractcalls import test_contract, add_creator, add_player, upload_content


class CreatorView(generics.ListCreateAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializers

    def post(self, request, *args, **kwargs):
        print(request.method)
        name = request.data["name"]
        description = request.data["description"]
        profilepic = request.data["profilepic"]
        add_creator(name, description, profilepic)
        return Response({"status": "Success"})


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

    def post(self, request, *args, **kwargs):
        print(request.method)
        name = request.data["name"]
        description = request.data["description"]
        age = request.data["age"]
        gender = request.data["gender"]
        location = request.data["location"]
        profilepic = request.data["profilepic"]
        sport = request.data["sport"]
        add_player(name, description, age, gender, location, profilepic, sport)
        return Response({"status": "Success"})


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

    def post(self, request, *args, **kwargs):
        print(request.method)
        playerId = request.data["player"]
        name = request.data["name"]
        file = request.data["file"]
        sport = request.data["sport"]
        upload_content(playerId, name, file, sport)
        return Response({"status": "Success"})


class ContentViewFilter(generics.ListAPIView):
    serializer_class = ContentSerilizers

    def get_queryset(self):
        contentCreator = self.request.query_params.get('contentCreator')
        return Content.objects.filter(contentCreator=contentCreator)


class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerilizers

##############################################


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilizers


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerilizers

##############################################


class CommentView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerilizers


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerilizers
