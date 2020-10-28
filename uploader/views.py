import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from MarsThinkTank.settings import STATIC_URL


@csrf_exempt
def getFile(request):
    if request.method == 'POST':
        myFile = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
        destination = open(os.path.join(STATIC_URL, myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        return render(request, "abstract/success.html")
    else:
        return render(request, "abstract/success.html")

def file_down(request):
    file=open(os.path.join(STATIC_URL, "最新激活码.txt"),'rb')
    response =HttpResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="ppp.txt"'
    return response