from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.generics import ListAPIView

from title.models import Title


class TitleView(ListAPIView):
    """
    返回所有title
    """

    def get(self, request):
        titleList = Title.objects.all()
        titleJsonList = []
        for item in titleList:
            titleJsonList.append(item.toJson())
        context = {"titleJsonList": titleJsonList}
        return render(request, "title/txt.html", context=context)


    def post(self, request):
        return HttpResponse("POST 方法")


