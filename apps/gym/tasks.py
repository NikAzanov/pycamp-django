from apps.gym import models
from config.celery import app
from libs.notifications.email import DefaultEmailNotification


@app.task
def send_notifications(attendees=None):
    if not attendees:
        attendees = models.Attendee.objects.all().select_related(
            "user",
            "gym",
            "gym__boss",
        )
    for attendee in attendees:
        DefaultEmailNotification(
            subject="Come back to the GYM",
            template="users/emails/notification.html",
            recipient_list=[attendee],
            user=attendee.user,
            gym=attendee.gym,
            boss=attendee.gym.boss,
        ).send()
