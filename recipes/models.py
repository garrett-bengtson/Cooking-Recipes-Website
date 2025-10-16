from django.db import models
from django.contrib.postgres.fields import ArrayField

class Recipe(models.Model):
    dishName = models.CharField(max_length=255)
    creatorName = models.CharField(max_length=255)
    ingredients = models.JSONField(default=list, blank=True)
    estimatedTime = models.IntegerField()
    directions = models.TextField()