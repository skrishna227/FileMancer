from celery import shared_task
import os
import shutil

@shared_task(queue='file_process_queue')
def backup_file(file_path):
    backup_path = f"{file_path}.bak"
    shutil.copy(file_path, backup_path)
    return backup_path

@shared_task(queue='file_process_queue')
def filedata_entry(file_path):
    # Simulate file data entry to the database
    # Here, you'd process the file and save data to the DB
    return f"Data from {file_path} entered into the database."

@shared_task(queue='file_process_queue')
def file_cleanup(file_path):
    os.remove(file_path)
    return f"{file_path} has been removed."
