from django.db import models

# Create your models here.
class UserSelection(models.Model):
    selection = models.CharField(max_length=100)

class Status(models.Model):
    stat = models.CharField(max_length=5)
    score = models.IntegerField()
    outoff = models.IntegerField()