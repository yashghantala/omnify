from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    max_capacity = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="events"
    )


class Attendee(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="attendees")

    class Meta:
        unique_together = ["email", "event"]
