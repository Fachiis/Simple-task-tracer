from rest_framework import serializers

from .models import Team, Task


class TeamSerializer(serializers.ModelSerializer):
    team_leader_id = serializers.IntegerField()

    class Meta:
        model = Team
        fields = ["id", "name", "team_leader_id", "team_members"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name", "team"]
