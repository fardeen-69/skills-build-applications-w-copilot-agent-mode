from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    members = serializers.ListField(child=serializers.EmailField(), required=False)
    class Meta:
        model = Team
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    user_email = serializers.CharField()
    class Meta:
        model = Activity
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField()
    class Meta:
        model = Workout
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField()
    class Meta:
        model = Leaderboard
        fields = '__all__'
