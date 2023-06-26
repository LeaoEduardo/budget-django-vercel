from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receive_date = models.DateField()
    source = models.CharField(max_length=50)
    value = models.FloatField()

class Card(models.Model):
    days = [(i,i) for i in range(1,29)]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    due_day = models.IntegerField(choices=days)

class Transaction(models.Model):
    TYPES = [
        ("I", "Incoming"),
        ("S", "Spending"),
    ]

    CATEGORIES = [
        ("Sa", "Salary"),
        ("Ho", "House"),
        ("C", "Car"),
        ("Sp", "Sports"),
        ("He", "Health"),
        ("M", "Market"),
        ("R", "Restaurants"),
        ("D", "Donations"),
        ("G", "Gifts"),
        ("E", "Entertainment"),
        ("O", "Other"),
    ]

    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=1, choices=TYPES)
    category = models.CharField(max_length=30, choices=CATEGORIES, default="Other")
    date = models.DateField(default=date.today)
    value = models.FloatField()
    description = models.TextField(null=True)