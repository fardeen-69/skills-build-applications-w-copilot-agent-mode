from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='activityuser', email='activityuser@example.com')
        activity = Activity.objects.create(user_email=user.email, type='run', duration=30, calories=300)
        self.assertEqual(activity.type, 'run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(username='workoutuser', email='workoutuser@example.com')
        workout = Workout.objects.create(user_email=user.email, name='Morning Routine', description='Pushups and squats', date='2024-01-01')
        self.assertEqual(workout.name, 'Morning Routine')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Leaderboard Team')
        leaderboard = Leaderboard.objects.create(team_name=team.name, score=100)
        self.assertEqual(leaderboard.score, 100)
