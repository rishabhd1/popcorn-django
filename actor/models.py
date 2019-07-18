from django.db import models
from django.urls import reverse


class Actor(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    sex = models.CharField(max_length=20)
    dateOfBirth = models.DateField()
    bio = models.TextField()
    image = models.ImageField(upload_to='images/actors/', default='images/no_image.png')

    def get_absolute_url(self):
        return reverse("actor_detail", kwargs={"id": self.id})
