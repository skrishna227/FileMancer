from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from . import models

# Create your views here.


class TaskAvailableView(View):
    def get(self, *args, **kwargs):
        task_list = models.TaskAvailableModel.objects.all().values()
        return HttpResponse(task_list)

