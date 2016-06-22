from django.db import models
from django.utils import timezone


class Buffet(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    desc = models.TextField()
    hrs_opening = models.TimeField()
    hrs_closing = models.TimeField()
    price = models.FloatField()
    child_price = models.FloatField()
    rating = models.FloatField()
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def update(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

        #calcuateeaveragerating