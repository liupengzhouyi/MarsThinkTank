"""MarsThinkTank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api import views
from index.views import indexPage

router = routers.DefaultRouter()
router.register('api_info', views.APIInfoViewSet)

from abstract.views import UserViewSet, GroupViewSet

router.register(r'users',UserViewSet)
router.register(r'groups',GroupViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="测试工程API",
        default_version='v1.0',
        description="测试工程接口文档",
        terms_of_service="#",
        contact=openapi.Contact(email="测试"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include(router.urls)),  # 代表位于根路径的主域名(http://127.0.0.1:8000)

    # 配置django-rest-framwork API路由
    url('api/', include('api.urls')),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # 配置drf-yasg路由
    url('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('index/', indexPage),

    path('userInformation/', include('userInformation.urls')),
    path('project/', include('project.urls')),
    path('abstract/', include('abstract.urls')),
    path('uploader/', include('uploader.urls')),
    path('title/', include('title.urls')),



    #url(r'^test1', CustomView.as_view(), name='test1'),

]
