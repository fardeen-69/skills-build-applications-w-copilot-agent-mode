from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        Activity.objects.all().delete()
        for team in Team.objects.all():
            if team.id is not None:
                team.delete()
        for user in User.objects.all():
            if user.id is not None:
                user.delete()

        # Create users (super heroes)
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com'},
            {'username': 'thor', 'email': 'thor@marvel.com'},
        ]
        dc_heroes = [
            {'username': 'batman', 'email': 'batman@dc.com'},
            {'username': 'superman', 'email': 'superman@dc.com'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com'},
        ]
        marvel_users = [User.objects.create_user(**hero) for hero in marvel_heroes]
        dc_users = [User.objects.create_user(**hero) for hero in dc_heroes]

        # Create teams
        marvel_team = Team.objects.create(name='Marvel', members=[u.email for u in marvel_users])
        dc_team = Team.objects.create(name='DC', members=[u.email for u in dc_users])

        # Create activities
        for user in marvel_users + dc_users:
            Activity.objects.create(user_email=user.email, type='Running', duration=30, calories=300)
            Activity.objects.create(user_email=user.email, type='Cycling', duration=45, calories=400)

        # Create workouts
        for user in marvel_users + dc_users:
            Workout.objects.create(user_email=user.email, name='Morning Cardio', description='Cardio session', date='2024-02-28')
            Workout.objects.create(user_email=user.email, name='Strength Training', description='Weights and resistance', date='2024-02-28')

        # Create leaderboard
        Leaderboard.objects.create(team_name=marvel_team.name, score=1000)
        Leaderboard.objects.create(team_name=dc_team.name, score=900)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
