# example/urls.py
from django.urls import path

from budget.views import index


urlpatterns = [
    path('', index),
]