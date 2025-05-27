from django.shortcuts import render
from rest_framework import status
from custom_utils.response import success_response, error_response
from custom_utils import message
from rest_framework.decorators import api_view
from .models import IncomeRecord
from .serializers import IncomeRecordSerializer
from django.core.exceptions import ObjectDoesNotExist

# Show all income records
@api_view(['GET'])
def show_income_records(request):
    try:
        records = IncomeRecord.objects.select_related(
            'transaction', 'account', 'category'
        ).all().order_by('-transaction__created_at')
        serializer = IncomeRecordSerializer(records, many=True)
        return success_response(data=serializer.data)
    except ObjectDoesNotExist:
        return error_response(message=message.DATA_NOT_FOUND, status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return error_response(message=message.GENERIC_ERROR)

