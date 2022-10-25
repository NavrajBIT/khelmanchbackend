from attr import fields
from rest_framework import serializers
from .models import Creator, Sport, Player, Content, User, Comment


class CreatorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = "__all__"


class SportSerializers(serializers.ModelSerializer):

    class Meta:
        model = Sport
        fields = "__all__"


class PlayerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = "__all__"


class ContentSerilizers(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Content
        fields = "__all__"


class UserSerilizers(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"


class CommentSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
