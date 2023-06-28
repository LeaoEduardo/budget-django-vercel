# example/urls.py
from django.urls import path, include

from budget.views import create_transaction, create_card, create_budget, dashboard_data_bar
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('transaction/create/', create_transaction, name='create_transaction' ),
    path('card/create/', create_card, name='create_card' ),
    path('budget/create/', create_budget, name='create_budget' ),
    path('dashboard-data-bar/', dashboard_data_bar, name='dashboard_data_bar' ),
    path('accounts/', include('django.contrib.auth.urls')),
]