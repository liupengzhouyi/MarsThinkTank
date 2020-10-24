from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

def indexPage(request):
    # 记载模板文件，生产模板对象
    template = loader.get_template('index/index.html')
    # 给定模板上下文，给模板文件传递数据
    context = {'numbers': list(range(1, 10))}
    # 模板渲染：产生标准的html文档
    res_html = template.render(context, request)
    # 返回
    return HttpResponse(res_html)