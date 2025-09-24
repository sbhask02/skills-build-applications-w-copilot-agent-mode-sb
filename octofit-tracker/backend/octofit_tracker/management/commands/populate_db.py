from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

# Sample models for demonstration
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User(email='tony@stark.com', name='Tony Stark', team='Marvel'),
            User(email='steve@rogers.com', name='Steve Rogers', team='Marvel'),
            User(email='clark@kent.com', name='Clark Kent', team='DC'),
            User(email='bruce@wayne.com', name='Bruce Wayne', team='DC'),
        ]
        for user in users:
            user.save()

        # Create activities
        activities = [
            Activity(user_email='tony@stark.com', activity_type='Running', duration=30),
            Activity(user_email='steve@rogers.com', activity_type='Cycling', duration=45),
            Activity(user_email='clark@kent.com', activity_type='Swimming', duration=60),
            Activity(user_email='bruce@wayne.com', activity_type='Boxing', duration=50),
        ]
        for activity in activities:
            activity.save()

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=110)

        # Create workouts
        workouts = [
            Workout(name='Super Strength', difficulty='Hard'),
            Workout(name='Flight Training', difficulty='Medium'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
