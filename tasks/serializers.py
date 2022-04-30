from unicodedata import name
from rest_framework import serializers

from .models import Team, Task


class TeamSerializer(serializers.ModelSerializer):
    team_leader_id = serializers.IntegerField()

    class Meta:
        model = Team
        fields = ["id", "name", "team_leader_id", "team_members"]


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "status"]


class TeamLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "team",
            "team_members",
            "status",
            "started_at",
            "completed_at",
        ]


class TaskSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "team",
            "status",
            "started_at",
            "completed_at",
        ]


class CreateTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ["name", "team"]
