from rest_framework.serializers import ModelSerializer

from event_management.models import Attendee, Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        exclude = ["created_by"]


class AttendeeSerializer(ModelSerializer):
    class Meta:
        model = Attendee
        exclude = ["event"]
