from rest_framework.views import exception_handler, Response
from django.core.exceptions import ValidationError


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None and isinstance(exc, ValidationError):
        return Response(status=400)
    return response
