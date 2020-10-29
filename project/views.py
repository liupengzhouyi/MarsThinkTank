from datetime import date, datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from project.mapper import ProjectMapper
from project.models import Project
from userInformation.models import UserInformation

def getProjectInformation(request):
    # 记载模板文件，生产模板对象
    template = loader.get_template('project/createProject/createProject.html')
    # 给定模板上下文，给模板文件传递数据
    context = {'numbers': list(range(1, 10))}
    # 模板渲染：产生标准的html文档
    res_html = template.render(context, request)
    # 返回
    return HttpResponse(res_html)


def createProject(request):
    project = Project()

    if 'projectName' in request.GET:
        project.name = request.GET['projectName']

    project.create_date = datetime.now()

    userInformationJson = request.session.get('userInformation', default=None)
    if userInformationJson is None:
        return render(request, "index/signIn/signIn.html")
    else:
        try:
            userInformationInDB = UserInformation.objects.filter(email=userInformationJson['email'])
            print(userInformationInDB)
            project.autherID = userInformationInDB[0].id
            project.save()
            return render(request, "project/createProject/success.html")
        except UserInformation.DoesNotExist:
            return render(request, "index/signIn/signIn.html")


def showMyProject(request):
    userInformationJson = request.session.get('userInformation', default=None)
    if userInformationJson is None:
        return render(request, "index/signIn/signIn.html")
    else:
        try:
            userInformationInDB = UserInformation.objects.filter(email=userInformationJson['email'])
            projects = Project.objects.filter(autherID=userInformationInDB[0].id)
            context = {"projects": projects}
            return render(request, "project/showProject/myProject.html", context=context)
        except UserInformation.DoesNotExist:
            return render(request, "index/signIn/signIn.html")




def getJsonData(request):
    userInformationJson = request.session.get('userInformation', default=None)
    if userInformationJson is None:
        return render(request, "index/signIn/signIn.html")
    else:
        try:
            userInformationInDB = UserInformation.objects.filter(email=userInformationJson['email'])
            projects = Project.objects.filter(autherID=userInformationInDB[0].id)
            content = {"projects": projects}
            projectSet = []
            for project in projects:
                projectSet.append(ProjectMapper(project))
            return JsonResponse(projectSet, safe=False)
        except UserInformation.DoesNotExist:
            return render(request, "index/signIn/signIn.html")

def projectInformation(request):
    projectInformationID = request.GET['projectInformationID']
    if projectInformationID is None:
        return render(request, "project/information/ProjectInformation.html")
    else:
        projectInformationInDB = Project.objects.filter(id = projectInformationID)
        return render(request, "project/information/ProjectInformation.html", context=ProjectMapper(projectInformationInDB[0]))

