from django.contrib import admin

from .models import Team, Task


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    autocomplete_fields = ["team_leader", "team_members"]
    list_display = ["name", "team_leader", "get_team_members"]
    search_fields = ["name"]

    def get_team_members(self, obj):
        return ", ".join([str(member) for member in obj.team_members.all()])


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    autocomplete_fields = ["team", "team_members"]
    list_editable = ["status"]
    list_select_related = ["team"]
    list_display = [
        "name",
        "team",
        "get_team_members",
        "status",
        "started_at",
        "completed_at",
    ]
    search_fields = ["name"]

    def get_team_members(self, obj):
        return ", ".join([str(member) for member in obj.team_members.all()])
