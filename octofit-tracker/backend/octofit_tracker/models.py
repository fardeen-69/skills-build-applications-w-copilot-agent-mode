from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Additional fields can be added here
    pass

from djongo import models as djongo_models

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField(default=list)  # Store user emails

class Activity(models.Model):
    user_email = models.CharField(max_length=100)  # Reference by email
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    calories = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Workout(models.Model):
    user_email = models.CharField(max_length=100)  # Reference by email
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

class Leaderboard(models.Model):
    team_name = models.CharField(max_length=100)  # Reference by team name
    score = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
