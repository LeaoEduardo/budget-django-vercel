from collections import defaultdict

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .forms import TransactionForm, CardForm, BudgetForm
from .models import Transaction
from .queries import get_current_month_transactions

def login(request):
    return auth_views.LoginView.as_view()

def logout(request):
    return auth_views.LogoutView.as_view()

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
    return render_form(request, TransactionForm, "/", "create", "Create Transaction")

@login_required()
def create_card(request):
    return render_form(request, CardForm, "/", "create", "Create Card")

@login_required()
def create_budget(request):
    return render_form(request, BudgetForm, "/", "create", "Create Budget")

@login_required()
def dashboard_data_bar(request):
    transactions = get_current_month_transactions()
    categories = dict((x,y) for x,y in Transaction.CATEGORIES)

    sum_by_categories = defaultdict(float)
    for category, value in [(t.category, t.value) for t in transactions]:
        sum_by_categories[categories[category]] += value

    sum_by_categories = dict(sum_by_categories)
    # Retrieve the necessary data from your backend
    labels = list(sum_by_categories.keys())
    values = list(sum_by_categories.values())

    # Create a dictionary containing the data
    data = {
        'x': labels,
        'y': values,
        'y_label': "Values",
        'canvas_id': "chart1"
    }

    return JsonResponse(data)
