from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .forms import TransactionForm, CardForm, BudgetForm

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