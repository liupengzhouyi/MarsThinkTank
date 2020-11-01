from .models import FileByLP
from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileByLP
        fields = '__all__'