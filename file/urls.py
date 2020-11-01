from django.conf.urls import url
from django.urls import path, include
from django.views.static import serve
from rest_framework import routers

from file.views import FileViewSet

router = routers.DefaultRouter()
router.register(r'upload', FileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]