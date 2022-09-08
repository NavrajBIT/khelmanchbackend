from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Creator(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    profilepic = models.ImageField(upload_to='images/')   


class Player(models.Model):
    profileCreator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    description = models.TextField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    fatherName = models.CharField(max_length=50)
    motherName = models.CharField(max_length=50)
    skillName = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    profilepic = models.ImageField(upload_to='images/')


class Content(models.Model):
    contentCreator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='videos/', null=True, verbose_name="")
    description = models.TextField()
    skillName = models.CharField(max_length=50)
    view_count = models.IntegerField(default=0, null=True, blank=True)


class Ratings(models.Model):

    content_rating = models.ForeignKey(
        Content, on_delete=models.CASCADE, blank=True, null=True)
    storing_prev_now_rated_value = models.IntegerField(
        null=True, blank=True, default=1)
    avg_rating = models.IntegerField(null=True, blank=True, default=1)
    count = models.IntegerField(blank=True, null=True)
    rated_number = models.IntegerField(blank=True, null=True, default=0,
                                       validators=[
                                           MaxValueValidator(5),
                                           MinValueValidator(1),
                                       ]
                                       )

    def __str__(self):
        return self.content_rating.name  # recheck
