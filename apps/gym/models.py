from django.db import models

from apps.core.models import BaseModel


class Gym(BaseModel):
    """Simple model for Gym."""
    name = models.CharField(
        max_length=64,
        verbose_name='Name',
    )
    boss = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
        related_name='own_gyms',
        verbose_name='Boss of the Gym',
    )
    description = models.TextField(
        blank=True,
        verbose_name='Description',
        max_length=1024,
    )
    attendees = models.ManyToManyField(
        to='users.User',
        through='gym.Attendee',
        related_name='gym_attendees',
        verbose_name='Attendees',
    )

    def __str__(self):
        return self.name


class Subscription(BaseModel):
    """Simple model for Subscription."""
    name = models.CharField(
        max_length=64,
    )
    gym = models.ForeignKey(
        to=Gym,
        on_delete=models.CASCADE,
        related_name='subscriptions',
        verbose_name='Gym',
    )

    def __str__(self):
        return self.name


class Attendee(BaseModel):
    """Intermediate model between `User` and `Gym`."""
    user = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
        related_name='gyms',
        verbose_name='User',
    )
    gym = models.ForeignKey(
        to=Gym,
        on_delete=models.CASCADE,
        verbose_name='Gym',
    )
    subscription = models.ForeignKey(
        to=Subscription,
        on_delete=models.SET_NULL,
        related_name='subscribers',
        verbose_name='Subscription',
        null=True,
    )

    def __str__(self):
        return f'Attendee {self.user} of {self.gym}'

    class Meta:
        unique_together = (
            'user', 'gym',
        )
