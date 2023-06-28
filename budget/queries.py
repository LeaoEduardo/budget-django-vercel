from datetime import date
from .models import *

def get_current_month_transactions():
    td = date.today()
    current_year = td.year
    current_month = td.month
    return Transaction.objects.filter(date__gte=date(current_year, current_month, 1))
