from django.contrib import admin
from .models import AlertModel

@admin.register(AlertModel)
class AlertAdmin(admin.ModelAdmin):
    list_display =('id', 'event', 'status', 'created_at')

# Register your models here.
