from django.db import connection
from django.db.utils import OperationalError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view([ "GET" ])
def health(request):
    try:
        connection.ensure_connection()
        return Response(status=status.HTTP_200_OK)
    except OperationalError:
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
