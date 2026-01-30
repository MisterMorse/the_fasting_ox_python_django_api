from django.db import connection
from django.db.utils import OperationalError

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view([ "GET" ])
def health_deployment(request):
    return Response({"status": "ok"})

@api_view([ "GET" ])
def health_database(request):
    try:
        connection.ensure_connection()
        return Response({"status": "ok"})
    except OperationalError as e:
        return Response({"error": str(e)})
