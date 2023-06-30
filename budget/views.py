from collections import defaultdict
import locale

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .forms import TransactionForm, CardForm, BudgetForm, GoalForm
from .models import Transaction
from .queries import *

# Admin
def login(request):
    return auth_views.LoginView.as_view()

def logout(request):
    return auth_views.LogoutView.as_view()

# CRUD and FORMS
@login_required()
def render_form(request, form_model, redirect_response, form_url, title):
    if request.method == "POST":
        form = form_model(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect(redirect_response)
    else:
        form = form_model()
    
    return render(request, "base_form.html", {"form": form, "form_url": form_url, "title": title})

@login_required()
def create_transaction(request):
    return render_form(request, TransactionForm, "/", "", "Create Transaction")

@login_required()
def create_card(request):
    return render_form(request, CardForm, "/", "", "Create Card")

@login_required()
def create_budget(request):
    return render_form(request, BudgetForm, "/", "", "Create Budget")

@login_required()
def create_goal(request):
    return render_form(request, GoalForm, "/", "", "Create Goal")

# DASHBOARDS
def spending_by_category_and_month(month):
    if month=="current":
        transactions = get_current_month_transactions()
    elif month=="last":
        transactions = get_last_month_transactions()
    else:
        raise Exception("Not implemented yet")
    
    categories = dict((x,y) for x,y in Transaction.CATEGORIES)

    sum_by_categories = defaultdict(float)
    for category, value in [(t.category, t.value) for t in transactions]:
        sum_by_categories[categories[category]] += value

    sum_by_categories = dict(sum_by_categories)
    labels = list(sum_by_categories.keys())
    values = list(sum_by_categories.values())

    return labels, values

def spending_by_category(chart_id: str):
    labels, values = get_current_month_transactions()

    # Create a dictionary containing the data
    return {
        'type': 'bar',
        'x': labels,
        'y': values,
        'y_label': "Values",
        'canvas_id': chart_id
    }

@login_required()
def dashboard(request):
    data = {}
    data["chart1"] = spending_by_category("chart1")
    
    return JsonResponse(data)

# HOME PAGE

def money_left():
    transactions = get_current_month_transactions()
    budget = get_current_month_budget()

    spent = sum([t.value for t in transactions])
    received = sum([b.value for b in budget])
    left = received - spent

    return {
        'value': locale.currency(left, grouping=True),
        'label': 'Money left',
    }

def goal_percentages():
    percentages_list = []
    for goal in get_goals():
        total_value = goal.total_value
        current_value = goal.initial_value
        goal_transactions = get_goal_transactions(goal.id)
        current_value += sum([t.value for t in goal_transactions])
    
        goal_percentage = (current_value / total_value) * 100  # Calculate progress percentage

        delta = relativedelta(goal.desired_date, td)
        months = delta.months + 12*delta.years
        value_per_month = (total_value-current_value)/months

        percentages_list.append({
            "id": f"goal_id{goal.id}",
            "name": goal.name,
            "percentage": goal_percentage,
            "months": months,
            "desired_date": goal.desired_date,
            "value_per_month": locale.currency(value_per_month, grouping=True),
            "current_value": locale.currency(current_value, grouping=True),
            "total_value": locale.currency(total_value, grouping=True),
        })

    return percentages_list

@login_required()
def home(request):

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    context = {
        "money_left": money_left(),
        "goal_percentages": goal_percentages()
    }
    return render(request, "home.html", context)