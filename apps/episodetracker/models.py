from django.db import models

class Show(models.Model):
    name = models.CharField(max_length=64)
    episode = models.PositiveSmallIntegerField(default=0)

