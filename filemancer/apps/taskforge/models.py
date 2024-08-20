from django.db import models

# Create your models here.


class TaskAvailableModel(models.Model):
    task_name = models.CharField(max_length=200, blank=False, null=False)
    c_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.task_name
