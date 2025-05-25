from django.db import models

# Category model (income or expense)
class Category(models.Model):
    class categoryType(models.TextChoices):
        INCOME = "Income"
        EXPENSE = "Expense"
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=20, choices=categoryType, default=categoryType.EXPENSE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    

# Account model
class Account(models.Model):
    name = models.CharField(max_length=200) 
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.name} = {self.balance}'


# Transaction type (income, expense, transfer)
class Transaction(models.Model):
    class transactionTypes(models.TextChoices):
        INCOME = "Income"
        EXPENSE = "Expense"
        TRANSFER = "Transfer"
    type = models.CharField(max_length=20, choices=transactionTypes, default=transactionTypes.EXPENSE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.type} - {self.amount} - {self.date}'
    

# Income record
class IncomeRecord(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, limit_choices_to={'type': Category.categoryType.INCOME}, on_delete=models.CASCADE)

    def __str__(self):
        return f"Income {self.transaction.amount} to {self.account.name}"


# Expense record
class ExpenseRecord(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, limit_choices_to={'type': Category.categoryType.EXPENSE}, on_delete=models.CASCADE)

    def __str__(self):
        return f"Expense {self.transaction.amount} from {self.account.name}"
    

# Transfer record
class TransferRecord(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    from_account = models.ForeignKey(Account, related_name='transfers_out', on_delete=models.CASCADE)
    to_account = models.ForeignKey(Account, related_name='transfers_in', on_delete=models.CASCADE)

    def __str__(self):
        return f"Transfer {self.transaction.amount} from {self.from_account.name} to {self.to_account.name}"