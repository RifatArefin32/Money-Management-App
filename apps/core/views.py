from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import IncomeRecord
from .serializers import IncomeRecordSerializer

# Show all income records
@api_view(['GET'])
def show_income_records(request):
    records = IncomeRecord.objects.all().order_by('-transaction__created_at')
    serializer = IncomeRecordSerializer(records, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

