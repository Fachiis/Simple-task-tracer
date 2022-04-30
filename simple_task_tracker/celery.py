import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simple_task_tracker.settings")

app = Celery("simple_task_tracker")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
