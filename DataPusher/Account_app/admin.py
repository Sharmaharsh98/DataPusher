from django.contrib import admin
from .models import User_Account

# Register your models here.
@admin.register(User_Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'account_id', 'email', 'name']