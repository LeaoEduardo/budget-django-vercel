from datetime import datetime
from django.forms import ModelForm, DateInput
from .models import Transaction, Card, Budget

class CustomDateInput(DateInput):
    input_type="date"

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        exclude = ["user"]
        widgets = {
            'date': CustomDateInput()
        }

class CardForm(ModelForm):
    class Meta:
        model = Card
        exclude = ["user"]
    
class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        exclude = ["user"]
        widgets = {
            'receive_date': CustomDateInput()
        }