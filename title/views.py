from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class TitleView(View):

    def get(self, request):
        return HttpResponse("GET 方法")

    def post(self, request):
        return HttpResponse("POST 方法")


