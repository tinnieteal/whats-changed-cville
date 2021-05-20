from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Place(models.Model):
    place_name = models.CharField(max_length=200, default="default place name")
    place_address = models.CharField(max_length=200, default="default place address")
    google_place_id = models.TextField(default="default google place id")

    def __str__(self):
        return(str(self.place_name))

    # @classmethod
    # def newPlace(cls, place_n):
    #     place = cls(place_name=place_n)
    #     return place

class Change(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    # place_name_change = models.CharField(max_length=200, default="default place name")
    covid_rating = models.CharField(max_length=200, default="4/5")
    place_change = models.TextField(default="No changes submitted yet.")
    submitting_user = models.CharField(max_length=200, default="default submitter")
    submission_time = models.DateTimeField('time submitted', default=timezone.now)

    def was_published_recently(self):
        now = timezone.now()

        return now - datetime.timedelta(days=3) <= self.submission_time <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Submitted recently?'

    def __str__(self):
        return(str(self.place_change))

class Comment(models.Model): #https://djangocentral.com/creating-comments-system-with-django/ -- referenced this tutorial for parts of the comments feature
    change = models.ForeignKey(Change, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return '{} by {}'.format(self.body, self.user_name)
        
class Leaderboard(models.Model): #https://stackoverflow.com/questions/1391601/django-how-to-create-a-leaderboard - a general guideline for us when starting to create the Django Leaderboard model. (StackOverflow)
    user = models.CharField(max_length=200)
    num_submissions = models.IntegerField()
    def __str__(self):
        return str(self.user)+ ": " + str(self.num_submissions)
