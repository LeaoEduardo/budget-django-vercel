from datetime import date

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receive_date = models.DateField()
    source = models.CharField(max_length=50)
    value = models.FloatField()

class Card(models.Model):
    days = [(i,i) for i in range(1,29)]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    due_day = models.IntegerField(choices=days)

class Transaction(models.Model):
    TYPES = [
        ("I", "Incoming"),
        ("S", "Spending"),
    ]
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=1, choices=TYPES)
    date = models.DateField(default=date.today)
    value = models.FloatField()