from django.db import models
from django.utils import timezone

class Buffet(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    desc = models.TextField()
    hrs_opening = models.TimeField(help_text="Please use the following format: <em>HH:MM:SS</em>. 24-hour format")
    hrs_closing = models.TimeField(help_text="Please use the following format: <em>HH:MM:SS</em>. 24-hour format.")
    price = models.FloatField(help_text="in S$")
    child_price = models.FloatField()
    rating = models.FloatField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

        #calcuateeaveragerating