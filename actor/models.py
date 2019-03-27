from django.db import models

class Actor (models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=20)
    dateOfBirth = models.DateField()
    bio = models.TextField()