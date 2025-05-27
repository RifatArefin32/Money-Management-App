from rest_framework.response import Response
from rest_framework import status
from . import message

def success_response(data, message=message.DATA_FOUND, status_code=status.HTTP_200_OK):
    return Response({
        "success": True,
        "message": message,
        "data": data
    }, status=status_code)

def error_response(error=None, message=message.GENERIC_ERROR, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR):
    return Response({
        "success": False,
        "message": message,
        "error": None
    }, status=status_code)
