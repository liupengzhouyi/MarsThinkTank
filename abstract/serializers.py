# 序列化
from rest_framework import serializers

from abstract.models import Abstract


class AbstractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Abstract
        fields = ['abstractType', 'fatherID', 'abstractFileType', 'downloadLink', 'create_date', 'autherID', 'isNew']
