from django.shortcuts import render
from rest_framework import status
from custom_utils.response import success_response, error_response
from custom_utils import message
from rest_framework.decorators import api_view
from .models import IncomeRecord, Account
from .serializers import IncomeRecordSerializer, AccountSerializer
from django.core.exceptions import ObjectDoesNotExist

# Show all income records
@api_view(['GET'])
def show_income_records(request):
    try:
        records = IncomeRecord.objects.select_related(
            'transaction', 'account', 'category'
        ).all().order_by('-transaction__created_at')
        serializer = IncomeRecordSerializer(records, many=True)
        return success_response(data=serializer.data, message=message.DATA_FETCH_SUCCESS)
    except ObjectDoesNotExist:
        return error_response(message=message.DATA_NOT_FOUND, status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return error_response()


# Show all accounts
@api_view(['GET'])
def show_accounts(request):
    try:
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return success_response(data=serializer.data, message=message.DATA_FETCH_SUCCESS)
    except ObjectDoesNotExist:
        return error_response(message=message.DATA_NOT_FOUND, status_code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return error_response()