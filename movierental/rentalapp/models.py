from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title
