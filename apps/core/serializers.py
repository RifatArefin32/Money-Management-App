from rest_framework import serializers
from .models import IncomeRecord, Transaction, Account, Category


# Transaction serializer
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['type', 'amount', 'description', 'date']

        def validate_amount(self, value):
            if self.amount <= 0:
                raise serializers.ValidationError("Amount must be greater than zero!")
            return value

# Account serializer
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name', 'balance']

# Category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'type']

# Income record serializer
class IncomeRecordSerializer(serializers.ModelSerializer):
    transaction = TransactionSerializer(read_only=True)
    account = AccountSerializer(read_only=True)
    category=CategorySerializer(read_only=True)
    class Meta:
        model = IncomeRecord
        fields = [
            'id',
            'transaction',
            'account',
            'category'
        ]