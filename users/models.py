from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER = "U"
    TEAM_LEADER = "L"
    TEAM_MEMBER = "M"
    USER_ROLES = [
        (USER, "User"),
        (TEAM_LEADER, "Team Leader"),
        (TEAM_MEMBER, "Team Member"),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=1, choices=USER_ROLES, default=USER)
