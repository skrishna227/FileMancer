from django.contrib import admin
from .models import FileUploadDetail

# Register your models here.

class FileUploadDetailAdmin(admin.ModelAdmin):
    list_display = ('file', 'upload_date', 'selected_tasks')
admin.site.register(FileUploadDetail, FileUploadDetailAdmin)
