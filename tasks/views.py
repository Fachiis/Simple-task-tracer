from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .tasks import send_email_task
from .models import Team, Task
from .serializers import (
    CreateTaskSerializer,
    TeamSerializer,
    TaskSerializer,
    TeamLeaderSerializer,
    TeamMemberSerializer,
)

User = get_user_model()


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.prefetch_related("team_members").all()
    serializer_class = TeamSerializer


class TaskViewSet(ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]

    def get_queryset(self):
        return (
            Task.objects.prefetch_related("team__team_members")
            .select_related("team__team_leader")
            .all()
        )

    def get_serializer_class(self):
        user_id = self.request.user.id

        if self.request.method == "POST":
            return CreateTaskSerializer

        elif self.request.method == "PUT":
            if user_id == User.objects.filter(role=User.TEAM_LEADER).values_list(
                "id", flat=True
            ):
                return TeamLeaderSerializer
            elif user_id in User.objects.filter(role=User.TEAM_MEMBER).values_list(
                "id", flat=True
            ):
                return TeamMemberSerializer

        return TaskSerializer

    def create(self, request, *args, **kwargs):
        user_id = self.request.user.id
        if user_id in User.objects.filter(role=User.TEAM_USER).values_list(
            "id", flat=True
        ):
            subject = "New Task Assigned"
            message = request.data["name"]
            from_email = request.user.email
            team_id = request.data["team"]
            team_leader_email = Team.objects.get(id=team_id).team_leader.email
            recipient_list = [team_leader_email]

            send_email_task.apply_async(
                args=[subject, message, from_email, recipient_list]
            )
            return super().create(request, *args, **kwargs)

        return Response(
            status=status.HTTP_403_FORBIDDEN,
            data={"detail": "You are not allowed to create task"},
        )
