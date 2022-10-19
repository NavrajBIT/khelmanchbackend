from rest_framework import serializers
from .models import Creator, Sport, Player, Content




class CreatorSerializers(serializers.ModelSerializer):
    # profilepic = serializers.ImageField(
    #     max_length=None,
    #     allow_empty_file=False,
    #     allow_null=False,
    #     use_url=True,
    #     required=False,
    # )

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
    class Meta:
        model = Content
        fields = "__all__"


# class RatingSerilizers(serializers.ModelSerializer):
#     class Meta:
#         model = Ratings
#         fields = "__all__"
