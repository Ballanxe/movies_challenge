from django.urls import include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import PersonViewSet

router = DefaultRouter()
router.register(r'person', PersonViewSet)

urlpatterns = [url(r'', include((router.urls, 'person'))), ]
