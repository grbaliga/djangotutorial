from django.db import models

class Musicdata(models.Model):
    artists = models.TextField()
    id = models.TextField(primary_key=True)
    name = models.TextField()
    popularity = models.FloatField()
    year = models.IntegerField()


