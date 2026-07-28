from django.urls import path

from .views import add_job

urlpatterns = [
    path("jobs/", add_job),
]

