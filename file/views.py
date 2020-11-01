# views.py
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser

from file.models import FileByLP
from file.serializers import FileSerializer


class FileViewSet(viewsets.ModelViewSet):

    queryset = FileByLP.objects.all()
    serializer_class = FileSerializer
