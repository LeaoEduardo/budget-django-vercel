from datetime import date
from dateutil.relativedelta import relativedelta
from .models import *

td = date.today()

concat_query_objects = lambda x,y : list(x) + list(y)

def get_current_month_transactions():
    return Transaction.objects.filter(date__gte=date(td.year, td.month, 1))

def get_last_month_transactions():
    return Transaction.objects.\
        filter(date__gte=date(td.year, td.month, 1)-relativedelta(months=1)).\
        filter(date__lt=date(td.year, td.month, 1))

def get_current_month_budget():
    recurring_budgets = Budget.objects.filter(recurring=True)
    current_month_non_reccuring_budgets = Budget.objects.filter(recurring=False).\
                                            filter(receive_date__gte=date(td.year, td.month, 1))
    return concat_query_objects(recurring_budgets, current_month_non_reccuring_budgets)

def get_goals():
    return Goal.objects.all()

def get_goal_transactions(goal_id):
    return Transaction.objects.filter(goal=goal_id)