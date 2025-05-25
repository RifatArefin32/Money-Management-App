from django.core.management.base import BaseCommand
from apps.core.models import Category, Account, Transaction, IncomeRecord, ExpenseRecord, TransferRecord
from faker import Faker
from datetime import date
from decimal import Decimal
import random

fake = Faker()

def random_decimal(min_val, max_val):
    return Decimal(str(round(random.uniform(min_val, max_val), 2)))

class Command(BaseCommand):
    help = 'Populate dummy data'

    def handle(self, *args, **kwargs):
        # Create income categories
        self.stdout.write("Creating income categories...")
        income_categories = [
            Category.objects.create(name="Salary", type=Category.categoryType.INCOME),
            Category.objects.create(name="Bonus", type=Category.categoryType.INCOME),
            Category.objects.create(name="Gift", type=Category.categoryType.INCOME),
        ]

        # Create expense categories
        self.stdout.write("Creating expense categories...")
        expense_categories = [
            Category.objects.create(name="House bill", type=Category.categoryType.EXPENSE),
            Category.objects.create(name="Parents", type=Category.categoryType.EXPENSE),
            Category.objects.create(name="Current bill", type=Category.categoryType.EXPENSE),
            Category.objects.create(name="Transportation", type=Category.categoryType.EXPENSE),
        ]

        # Create accounts
        self.stdout.write("Creating accounts...")
        accounts = [
            Account.objects.create(name="Cash", balance=random_decimal(1000, 10000)),
            Account.objects.create(name="Personal Savings", balance=random_decimal(1000, 10000)),
            Account.objects.create(name="Health Savings", balance=random_decimal(1000, 10000)),
        ]

        # Create income records
        self.stdout.write("Creating income records...")
        for _ in range(10):
            account = random.choice(accounts)
            category = random.choice(income_categories)
            amount = Decimal("500.00")
            transaction = Transaction.objects.create(
                type=Transaction.transactionTypes.INCOME,
                amount=amount,
                description=fake.sentence(),
                date=date.today()
            )
            IncomeRecord.objects.create(transaction=transaction, account=account, category=category)
            account.balance += amount
            account.save()

        # Create expense records
        self.stdout.write("Creating expense records...")
        for _ in range(10):
            account = random.choice(accounts)
            category = random.choice(expense_categories)
            amount = Decimal("500.00")
            transaction = Transaction.objects.create(
                type=Transaction.transactionTypes.EXPENSE,
                amount=amount,
                description=fake.sentence(),
                date=date.today()
            )
            ExpenseRecord.objects.create(transaction=transaction, account=account, category=category)
            account.balance -= amount
            account.save()

        # Create transfer records
        self.stdout.write("Creating transfer records...")
        for _ in range(5):
            from_account, to_account = random.sample(accounts, 2)
            amount = random_decimal(100, 1000)
            transaction = Transaction.objects.create(
                type=Transaction.transactionTypes.TRANSFER,
                amount=amount,
                description=fake.sentence(),
                date=fake.date_between(start_date='-30d', end_date='today')
            )
            TransferRecord.objects.create(transaction=transaction, from_account=from_account, to_account=to_account)
            from_account.balance -= amount
            to_account.balance += amount
            from_account.save()
            to_account.save()

        self.stdout.write(self.style.SUCCESS("Dummy data generated successfully."))
