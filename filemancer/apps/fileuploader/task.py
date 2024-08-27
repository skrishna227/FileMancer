from celery import shared_task
import os 
from django.core.files.storage import default_storage
from django.conf import settings


@shared_task(queue='file_upload_queue')
def file_upload_task(file_name, file_data):
    file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', file_name)
    with default_storage.open(file_path, 'wb+') as destination:
            destination.write(file_data)
