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
    recurring = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.source}-{self.value}-{self.receive_date}"

class Card(models.Model):
    days = [(i,i) for i in range(1,29)]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    due_day = models.IntegerField(choices=days)

    def __str__(self):
        return self.name

class Transaction(models.Model):

    CATEGORIES = [
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

    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, choices=CATEGORIES, default="Other")
    date = models.DateField(default=date.today)
    value = models.FloatField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.category}-R${round(self.value)}-{self.date}"