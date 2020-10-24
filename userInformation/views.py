from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def sayHelloAt20200626(request):
    return HttpResponse("Hello World")