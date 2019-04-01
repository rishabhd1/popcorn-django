from django.db import models
from producer.models import Producer
from actor.models import Actor

class Movie (models.Model):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=False)
    yearOfRelease = models.CharField(max_length=4, blank=False, null=False)
    plot = models.TextField()
    poster = models.ImageField(upload_to='images/movies/', default='images/no_image.png')
    actors = models.ManyToManyField(Actor, blank=False)