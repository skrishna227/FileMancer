from django.urls import path
from . import views

urlpatterns = [
    path('', views.UploadFileClass.as_view(), name='file_uploader'),
    path('file-details/', views.UploadedFileDetail.as_view(), name='uploaded_file_details'),
]