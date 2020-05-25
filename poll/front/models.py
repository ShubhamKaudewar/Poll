from django.db import models

# Create your models here.
class Values(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    time = models.TextField(blank=True)
    view = models.TextField(blank=True)