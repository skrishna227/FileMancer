from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponseRedirect
from .forms import FileUploadForm
from celery import chain
from django.views.generic import View, ListView
import json
from .models import FileUploadDetail
import os
from .task import file_upload_task


class UploadFileClass(View):
    def get(self, *args, **kwargs):
        form = FileUploadForm()
        return render(self.request, 'fileuploader/uploader.html', {'form': form})
    def post(self, *args, **kwargs):
        form = FileUploadForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            file = self.request.FILES['file']
            tasks = json.dumps(form.cleaned_data['tasks'])
            file_upload_task.delay(file.name, file.read()) 

            saveobj = FileUploadDetail(file=file.name, selected_tasks=tasks)
            saveobj.save()

        return HttpResponseRedirect(self.request.path_info)


class UploadedFileDetail(ListView):
    model = FileUploadDetail
    template_name = 'fileuploader/uploaded-file-detail.html' 
    context_object_name = 'file_upload_context'  
    paginate_by = 5


