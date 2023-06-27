# example/urls.py
from django.urls import path, include

from budget.views import create_transaction, create_card, create_budget
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('transaction/create', create_transaction, name='create_transaction' ),
    path('card/create', create_card, name='create_card' ),
    path('budget/create', create_budget, name='create_budget' ),
    path('accounts/', include('django.contrib.auth.urls')),
]