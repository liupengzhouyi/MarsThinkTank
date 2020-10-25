
from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.
from django.template import loader

from userInformation.models import UserInformation


def sayHelloAt20200626(request):
    return HttpResponse("Hello World")


def signIn(request):
    # 记载模板文件，生产模板对象
    template = loader.get_template('index/signIn.html')
    # 给定模板上下文，给模板文件传递数据
    context = {'numbers': list(range(1, 10))}
    # 模板渲染：产生标准的html文档
    res_html = template.render(context, request)
    # 返回
    return HttpResponse(res_html)

def register(request):
    # 记载模板文件，生产模板对象
    template = loader.get_template('index/register/register.html')
    # 给定模板上下文，给模板文件传递数据
    context = {'numbers': list(range(1, 10))}
    # 模板渲染：产生标准的html文档
    res_html = template.render(context, request)
    # 返回
    return HttpResponse(res_html)


# 创建或修改 session：
# request.session[key] = value
# 获取 session：
# request.session.get(key,default=None)
# 删除 session
# del request.session[key] # 不存在时报错

def getRegisterInformation(request):
    request.encoding = 'utf-8'
    if 'passwordI' in request.GET:
        userInformation = UserInformation()
        userInformation.name = request.GET['username']
        userInformation.password = request.GET['passwordI']
        userInformation.phoneNumber = request.GET['phoneNumber']
        userInformation.email = request.GET['email']
        if request.GET['passwordI'] != request.GET['passwordII']:
            context = {'userInformation': userInformation, 'errorInformation': -1}
            return render(request, "index/register/fied.html", context)
        else:
            request.session['userInformation'] = userInformation.toJson()
            context = {'userInformation': userInformation, 'errorInformation': 0}
            return render(request, "index/register/registerInformation.html", context)
    else:
        userInformation = UserInformation()
        context = {'userInformation': userInformation,  'errorInformation': 1}
        return render(request, "index/register/fied.html", context)

def trueRegister(request):
    userInformationJson = request.session.get('userInformation',default=None)
    userInformation = UserInformation()

    userInformation.name = userInformationJson['name']
    userInformation.password = userInformationJson['password']
    userInformation.email = userInformationJson['email']
    userInformation.phoneNumber = userInformationJson['phoneNumber']

    
    userInformation.save()
    return render(request, "index/register/success.html")