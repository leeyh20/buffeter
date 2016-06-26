from django.db import models
from django.utils import timezone


# TO DO: LINK TO SOME GOVT DATA API AND TURN IT INTO THIS TUPLE
LOCATION_CHOICES = (
    ('Jurong East', 'Jurong East'),
    ('Bukit Batok', 'Bukit Batok'),
    ('Bukit Gombak', 'Bukit Gombak'),
    ('Choa Chu Kang', 'Choa Chu Kang'),
)
class Buffet(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, choices=LOCATION_CHOICES)
    desc = models.TextField()
    hrs_opening = models.TimeField(help_text="Please use the following format: <em>HH:MM:SS</em>. 24-hour format")
    hrs_closing = models.TimeField(help_text="Please use the following format: <em>HH:MM:SS</em>. 24-hour format.")
    price = models.FloatField(help_text="in S$")
    child_price = models.FloatField(default="", blank=True, null=True)
    rating = models.FloatField(help_text = "0 to 1, where 0 is no stars and 1 is 5 stars")
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
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

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
    buffet = models.ForeignKey(Buffet, related_name='reviews')
    #pub_date = models.DateTimeField('date published')
    created_date = models.DateTimeField(default=timezone.now)
    user_name = models.CharField(max_length=200)
    comment = models.TextField()
    approved_review = models.BooleanField(default=False)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def approve(self):
        self.approved_review = True
        self.save()

    def __str__(self):
        return self.comment