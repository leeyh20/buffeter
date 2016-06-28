from django.db import models
from django.utils import timezone

import statistics

# TO DO: LINK TO SOME GOVT DATA API AND TURN IT INTO THIS TUPLE
LOCATION_CHOICES = (
    ('Jurong East', 'Jurong East'),
    ('Bukit Batok', 'Bukit Batok'),
    ('Bukit Gombak', 'Bukit Gombak'),
    ('Choa Chu Kang', 'Choa Chu Kang'),
    ('Yew Tee', 'Yew Tee'),
    ('Kranji', 'Kranji'),
    ('Marsiling', 'Marsiling'),
    ('Woodlands', 'Woodlands'),
    ('Admiralty', 'Admiralty'),
    ('Sembawang', 'Sembawang'),
    ('Yishun', 'Yishun'),
    ('Khatib', 'Khatib'),
    ('Yio Chu Kang', 'Yio Chu Kang'),
    ('Ang Mo Kio', 'Ang Mo Kio'),
    ('Bishan', 'Bishan'),
    ('Braddell', 'Braddell'),
    ('Toa Payoh', 'Toa Payoh'),
    ('Novena', 'Novena'),
    ('Newton', 'Newton'),
    ('Orchard', 'Orchard'),
    ('Somerset', 'Somerset'),
    ('Dhoby Ghaut', 'Dhoby Ghaut'),
    ('City Hall', 'City Hall'),
    ('Raffles Place', 'Raffles Place'),
    ('Marina Bay', 'Marina Bay'),
    ('Marina South Pier', 'Marina South Pier'),

)

CUISINE_CHOICES = (
    ('International', 'International'),
    ('Korean BBQ', 'Korean BBQ'),
    ('Japanese Steamboat', 'Japanese Steamboat'),
    ('Vegeterian', 'Vegeterian'),

    )

class Buffet(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, choices=LOCATION_CHOICES)
    cuisine_type = models.CharField(max_length=200, choices=CUISINE_CHOICES)
    desc = models.TextField()
    hrs_opening = models.TimeField(help_text="Please use the following format: <em>HH:MM:SS</em>. 24-hour format")
    hrs_closing = models.TimeField(help_text="Please use the following format: <em>HH:MM:SS</em>. 24-hour format.")
    phone_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    
    weekday_adult_breakfast_price = models.FloatField(help_text="in S$", blank=True, null=True)
    weekday_adult_lunch_price = models.FloatField(help_text="in S$", null=True)
    weekday_adult_hightea_price = models.FloatField(help_text="in S$", blank=True, null=True)
    weekday_adult_dinner_price = models.FloatField(help_text="in S$", null=True)

    weekday_child_breakfast_price = models.FloatField(help_text="in S$", blank=True, null=True)
    weekday_child_lunch_price = models.FloatField(help_text="in S$", blank=True, null=True)
    weekday_child_hightea_price = models.FloatField(help_text="in S$", blank=True, null=True)
    weekday_child_dinner_price = models.FloatField(help_text="in S$", blank=True, null=True)

    weekend_adult_breakfast_price = models.FloatField(help_text="in S$", blank=True, null=True)
    weekend_adult_lunch_price = models.FloatField(help_text="in S$", null=True)
    weekend_adult_hightea_price = models.FloatField(help_text="in S$", blank=True, null=True)
    weekend_adult_dinner_price = models.FloatField(help_text="in S$", null=True)

    weekend_child_breakfast_price = models.FloatField(help_text="in S$", blank=True, null=True)
    weekend_child_lunch_price = models.FloatField(help_text="in S$", blank=True, null=True)
    weekend_child_hightea_price = models.FloatField(help_text="in S$", blank=True, null=True)
    weekend_child_dinner_price = models.FloatField(help_text="in S$", blank=True, null=True)

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
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.reviews.filter(approved_review=True))
        if (self.reviews.count() > 0):
            return '{:03.2f}'.format(statistics.mean(all_ratings))
        return 0.0

    def approved_reviews(self):
        return self.reviews.filter(approved_review=True)


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    author = models.ForeignKey('auth.User')
    buffet = models.ForeignKey(Buffet, related_name='reviews')
    #pub_date = models.DateTimeField('date published')
    created_date = models.DateTimeField(default=timezone.now)
    comment = models.TextField()
    approved_review = models.BooleanField(default=False)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def approve(self):
        self.approved_review = True
        self.save()

    def __str__(self):
        return self.comment