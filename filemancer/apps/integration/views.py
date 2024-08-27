from django.shortcuts import render
from django.views.generic import View
from .models import IntegrationListModel

# Create your views here.

class IntegrationListView(View):
    def get(self, *args, **kwargs):
        integration_list = IntegrationListModel.objects.all()
        integration_context = {"integration_list": integration_list}
        return render (self.request, "integration/integration_list.html", integration_context)

# class Integration
