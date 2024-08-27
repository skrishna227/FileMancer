from django.shortcuts import render
from django.http import JsonResponse
from .tasks import backup_file, filedata_entry, file_cleanup
from .forms import FileUploadForm
from celery import chain
import os
print("dzfxcgvhkjj",os.getcwd())
cwd = os.getcwd()

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_path = f"{cwd}/uploaded_files/{file.name}"
            
            # with open(file_path, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            
            tasks = form.cleaned_data['tasks']
            task_chain = []

            if 'backup' in tasks:
                task_chain.append(backup_file.s(file_path))
            if 'data_entry' in tasks:
                task_chain.append(filedata_entry.s())
            if 'cleanup' in tasks:
                task_chain.append(file_cleanup.s(file_path))

            if task_chain:
                result = chain(*task_chain)()
                return JsonResponse({"task_id": result.id})

    else:
        form = FileUploadForm()

    return render(request, 'taskforge/upload.html', {'form': form})


 