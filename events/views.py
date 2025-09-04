from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .factories import EventFactory
from .models import Event
from .serializers import EventSerializer


class CustomEventsResponse(Response):
    def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False, **kwargs):
        events = sorted(data, key=lambda x: x['date'])
        events = sorted(events, key=lambda x: x['start_time'])
        custom_data = {
            'events': events,
            **kwargs
        }
        super().__init__(custom_data, status=status, template_name=template_name, headers=headers, exception=exception)


@api_view(['GET'])
def event_list(request):
    query_set = Event.objects.all()
    serializer = EventSerializer(query_set, many=True)
    return CustomEventsResponse(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        EventFactory()
        serializer = EventSerializer(event)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EventSerializer(event, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        event.delete()
        return HttpResponse(status=204)

    else:
        return HttpResponse(status=404)
