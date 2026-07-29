from django.urls import path

from .views import JobHistoryAPIView, add_job

urlpatterns = [
    path("jobs/", add_job),
]


from rest_framework.routers import DefaultRouter
from .views import JobViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet)

urlpatterns = router.urls

