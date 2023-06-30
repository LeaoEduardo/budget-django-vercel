# example/urls.py
from django.urls import path, include

from budget.views import *
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', home, name='home'),
    path('transaction/create/', create_transaction, name='create_transaction' ),
    path('card/create/', create_card, name='create_card' ),
    path('budget/create/', create_budget, name='create_budget' ),
    path('goal/create/', create_goal, name='create_goal' ),
    path('dashboard/', dashboard, name='dashboard' ),
    path('accounts/', include('django.contrib.auth.urls')),
]