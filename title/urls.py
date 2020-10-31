
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.conf.urls import url

from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path("login/", views.TitleView.as_view()),

]