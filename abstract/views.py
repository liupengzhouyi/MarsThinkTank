from django.shortcuts import render

# Create your views here.
from abstract.models import Abstract




def createAbstract(abstract):
    abstract.save()


def findLastAbstract(abstractType, fatherID) ->Abstract:
    try:
        abstract = Abstract.objects.filter(abstractType=abstractType, fatherID=fatherID)
    except Abstract.DoesNotExist:
        abstract = None
    return abstract

def updateLastAbstract(abstract):
    try:
        abstractOrd = Abstract.objects.filter(abstractType=abstract.abstractType, fatherID=abstract.fatherID, isNew=1)
        if abstractOrd is None:
            abstract.save()
        else:
            abstractOrd.isNew = 0
            abstractOrd.sive()
            abstract.save()
    except Abstract.DoesNotExist:
        abstract.save()

def testFileUpload(request):
    return render(request, "abstract/FileUpload.html")

def create(request):
    return render(request, "abstract/createAbstract.html")





