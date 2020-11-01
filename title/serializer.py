from rest_framework import serializers

from title.models import Title


class CreateTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = ['name', 'createDateTime', 'authorID']
