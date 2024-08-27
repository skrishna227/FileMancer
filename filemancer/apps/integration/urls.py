from django.urls import path
from .views import IntegrationListView

urlpatterns = [
    path('', IntegrationListView.as_view(), name="integration"),
]