from django.db import models

# Create your models here.

class IntegrationListModel(models.Model):
    inte_name = models.CharField(max_length=100, blank=False, null=False)
    inte_client = models.CharField(max_length=100, blank=False, null=False, default="test_client")
    inte_start_time = models.DateTimeField(auto_now_add=True)
    source_path = models.CharField(max_length=1000, blank=False, null=False)
    output_path = models.CharField(max_length=1000, blank=False, null=False)
    
    auto_run = models.BooleanField(default=False)
    action = models.CharField(max_length=100, blank=False, null=False)