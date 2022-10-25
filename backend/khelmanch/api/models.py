import email
from email.policy import default
from django.db import models


def save_image(instance, *args, **kwargs):
    try:
        return "/".join(["images", str(instance.playerid), "profile.png"])
    except:
        return "/".join(["images", str(instance.address), "profile.png"])


def save_video(instance, filename, *args, **kwargs):
    return "/".join(["videos", str(instance.id), filename])


class Creator(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    profilepic = models.ImageField(
        upload_to=save_image, default="profilepic.jpg")
    address = models.CharField(primary_key=True, max_length=50, unique=True)
    rating = models.FloatField(default=0.0)


class Sport(models.Model):
    name = models.CharField(max_length=50)


class Player(models.Model):
    playerid = models.CharField(max_length=100, primary_key=True)
    profileCreator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    sport = models.ForeignKey(Sport, null=True, on_delete=models.SET_NULL)
    profilepic = models.ImageField(
        upload_to=save_image, default="profilepic.jpg")


class Content(models.Model):
    contentCreator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to=save_video, verbose_name="")
    sport = models.ForeignKey(Sport, null=True, on_delete=models.SET_NULL)
    view_count = models.IntegerField(default=0, null=True, blank=True)
    rating = models.FloatField(default=0.0)


class User(models.Model):
    name = models.CharField(max_length=50)
    email_id = models.CharField(max_length=25)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    profilepic = models.ImageField(
        upload_to='images/', default="profilepic.jpg")


class Comment(models.Model):
    content = models.ForeignKey(
        Content, on_delete=models.CASCADE, related_name='comments')
    commentCreator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
