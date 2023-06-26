from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Budget, Card, Transaction

admin.site.register(User, UserAdmin)
admin.site.register(Budget) 
admin.site.register(Card) 
admin.site.register(Transaction)


