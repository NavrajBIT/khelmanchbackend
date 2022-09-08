from rest_framework import serializers
from .models import Creator, Player, Content, Ratings


class CreatorSerializers(serializers.ModelSerializer):
    profilepic = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=False, use_url=True, required=False)

    class Meta:
        model = Creator
        fields = ('__all__')


class PlayerSerializers(serializers.ModelSerializer):
    profilepic = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=False, use_url=True, required=False)

    class Meta:
        model = Player
        fields = ('__all__')


class ContentSerilizers(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ('__all__')


class RatingSerilizers(serializers.ModelSerializer):

    class Meta:
        model = Ratings
        fields = ('__all__')
