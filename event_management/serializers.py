from django.utils import timezone
from rest_framework.serializers import ModelSerializer, ValidationError

from event_management.models import Attendee, Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        exclude = ["created_by"]

    def validate(self, attrs):
        """
        Validates start and end time of a event.
        """

        start_time = attrs.get("start_time")
        end_time = attrs.get("end_time")
        current_time = timezone.now()

        if start_time < current_time:
            raise ValidationError({"start_time": "Start time must be of future."})

        if end_time < start_time:
            raise ValidationError({"end_time": "End time must be later to start time."})

        return attrs


class AttendeeSerializer(ModelSerializer):
    class Meta:
        model = Attendee
        exclude = ["event"]
