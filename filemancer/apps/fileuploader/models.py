from django.db import models

# Create your models here.

class FileUploadDetail(models.Model):
    file = models.FileField(upload_to='uploads/')
    upload_date = models.DateTimeField(auto_now_add=True)
    selected_tasks = models.JSONField() 
