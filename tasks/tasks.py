from celery import shared_task

from .email import send_email


@shared_task
def send_email_task(subject, message, from_email, recipient_list):
    send_email(subject, message, from_email, recipient_list)
    return
