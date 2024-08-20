from django.urls import path
from . import views

urlpatterns = [
    path('task-available/', views.TaskAvailableView.as_view(), name="TaskAvailableView"),
]