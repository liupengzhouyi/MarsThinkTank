import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from MarsThinkTank.settings import STATIC_URL


@csrf_exempt
def getFile(request):
    print('rctfvygbuhnj')
    if request.method == 'POST':
        obj = request.FILES['file']
        myFile = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
        destination = open(os.path.join('././tempFilePath', myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

        return render(request, "abstract/success.html")
    else:
        ret = {'status': True, 'path': 'null'}
        return render(request, "abstract/success.html")



def gg(request):
    # 记载模板文件，生产模板对象
    template = loader.get_template('abstract/success.html')
    # 给定模板上下文，给模板文件传递数据
    context = {'numbers': list(range(1, 10))}
    # 模板渲染：产生标准的html文档
    res_html = template.render(context, request)
    # 返回
    return HttpResponse(res_html)
    # return render(request, "abstract/success.html")



