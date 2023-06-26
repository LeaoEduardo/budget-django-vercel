# example/urls.py
from django.urls import path, include

from budget.views import index, form_sent


urlpatterns = [
    path('', index),
    path('form-sent', form_sent),
]