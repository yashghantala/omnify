from django.utils import timezone

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from rest_framework.viewsets import GenericViewSet

from event_management.models import Attendee, Event
from event_management.paginators import CustomResultsSetPagination
from event_management.serializers import AttendeeSerializer, EventSerializer


class EventViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomResultsSetPagination

    def get_queryset(self):
        return Event.objects.all()

    def create(self, request, **kwargs):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        event_data = serializer.validated_data
        event = Event()
        event.name = event_data.get("name")
        event.location = event_data.get("location")
        event.max_capacity = event_data.get("max_capacity")
        event.start_time = event_data.get("start_time")
        event.end_time = event_data.get("end_time")
        event.created_by = request.user
        event.save()

        return Response(status=HTTP_201_CREATED)

    def list(self, request, **kwargs):
        events = Event.objects.filter(
            created_by=request.user, start_time__gt=timezone.now()
        )
        events = EventSerializer(events, many=True).data

        return Response(data=events)

    @action(methods=["POST"], detail=True)
    def register(self, request, pk=None):
        serializer = AttendeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        attendee_data = serializer.validated_data

        try:
            event = Event.objects.get(pk=pk, created_by=request.user)
        except Event.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        attendee = Attendee()
        attendee.name = attendee_data.get("name")
        attendee.email = attendee_data.get("email")
        attendee.event = event
        attendee.save()

        return Response(status=HTTP_201_CREATED)

    @action(methods=["GET"], detail=True)
    def attendees(self, request, pk=None):
        event = None

        try:
            event = Event.objects.get(pk=pk, created_by=request.user)
        except Event.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        attendees = event.attendees.all()
        page = self.paginate_queryset(attendees)
        data = AttendeeSerializer(page, many=True).data
        response = self.get_paginated_response(data)

        return response
