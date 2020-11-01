from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView

from abstract.models import Abstract
# Create your views here.
from abstract.serializers import AbstractSerializer


class createAbstract(CreateAPIView):
    '''
    Create Abstract
    '''

    serializer_class = AbstractSerializer



class abstractList(ListAPIView):
    '''get abstract list'''

    queryset = Abstract.objects.all()
    serializer_class = AbstractSerializer



