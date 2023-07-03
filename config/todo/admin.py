from django.contrib import admin
from .models import Todo, Account

admin.site.register(Account)
# Register your models here.
admin.site.register(Todo)