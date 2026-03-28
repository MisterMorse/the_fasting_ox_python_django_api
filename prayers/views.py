from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Prayer
from .serializers import PrayerSerializer


class CustomPrayersResponse(Response):
    def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False, **kwargs):
        prayers = sorted(data, key=lambda x: x[ "category" ])
        custom_data = {
            "prayers": prayers,
            **kwargs
        }
        super().__init__(custom_data, status=status, template_name=template_name, headers=headers, exception=exception)


@api_view([ "GET" ])
def prayer_list(request):
    query_set = Prayer.objects.all()
    serializer = PrayerSerializer(query_set, many=True)
    return CustomPrayersResponse(serializer.data)
