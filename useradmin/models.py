from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.ForeignKey(User, unique=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    profile_pic = models.ImageField(upload_to = 'profile', null=True)

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

