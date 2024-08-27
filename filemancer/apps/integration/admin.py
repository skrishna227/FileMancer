from django.contrib import admin
from .models import IntegrationListModel


# Register your models here.

class IntegrationListModelAdmin(admin.ModelAdmin):
    list_display = ('inte_name', 'inte_client', 'inte_start_time', 'auto_run', 'action')
admin.site.register(IntegrationListModel, IntegrationListModelAdmin)

