from rest_framework.viewsets import ModelViewSet

from .models import Team, Task
from .serializers import TeamSerializer, TaskSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.prefetch_related("team_members").all()
    serializer_class = TeamSerializer


class TaskViewSet(ModelViewSet):
    # TODO: update taskapi with given requirements
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
