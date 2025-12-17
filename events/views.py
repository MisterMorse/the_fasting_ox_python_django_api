from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Event
from .serializers import EventSerializer


class CustomEventsResponse(Response):
    def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False, **kwargs):
        events = sorted(data, key=lambda x: x[ "date" ])
        custom_data = {
            "events": events,
            **kwargs
        }
        super().__init__(custom_data, status=status, template_name=template_name, headers=headers, exception=exception)


@api_view([ "GET" ])
def event_list(request):
    query_set = Event.objects.all()
    serializer = EventSerializer(query_set, many=True)
    return CustomEventsResponse(serializer.data)


@api_view([ "GET" ])
def event_list_by_category(request, category):
    query_set = Event.objects.all().filter(category=category)
    serializer = EventSerializer(query_set, many=True)
    return CustomEventsResponse(serializer.data)
