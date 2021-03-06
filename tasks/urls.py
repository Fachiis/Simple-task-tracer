from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("teams", views.TeamViewSet, basename="teams")
router.register("tasks", views.TaskViewSet, basename="tasks")

urlpatterns = router.urls
