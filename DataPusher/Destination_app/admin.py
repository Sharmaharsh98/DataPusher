from django.contrib import admin
from .models import Destination_model

# Register your models here.
@admin.register(Destination_model)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']