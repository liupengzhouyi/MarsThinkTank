"""LearnDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from project.views import createProject
from project.views import showMyProject
from project.views import getJsonData
from project.views import projectInformation



schema_view = get_swagger_view(title="Project API")


urlpatterns = [

    path('createProject/', createProject),
    path('showMyProject/', showMyProject),
    path('getJsonData/', getJsonData),
    path('projectInformation/', projectInformation),







]
