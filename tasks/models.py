from django.db import models
from django.conf import settings


class Team(models.Model):
    name = models.CharField(max_length=255)
    team_leader = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="team_leader"
    )
    team_members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="members"
    )

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    TASK_ASSIGNED = "A"
    TASK_IN_PROGRESS = "P"
    TASK_UNDER_REVIEW = "R"
    TASK_DONE = "D"
    TASK_CHOICES = [
        (TASK_ASSIGNED, "Assigned"),
        (TASK_IN_PROGRESS, "In Progress"),
        (TASK_UNDER_REVIEW, "Under Review"),
        (TASK_DONE, "Done"),
    ]
    name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="tasks")
    team_members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="team_members"
    )
    status = models.CharField(max_length=1, choices=TASK_CHOICES, default=TASK_ASSIGNED)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
