from rest_framework.response import Response
from rest_framework.decorators import api_view

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
