from django.contrib import admin
from .models import TaskAvailableModel

# Register your models here.


class TaskAvailableModelAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'description')
admin.site.register(TaskAvailableModel, TaskAvailableModelAdmin)
