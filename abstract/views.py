from django.shortcuts import render

# Create your views here.
from django.views import View

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




from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from abstract.serializers import UserSerializer,GroupSerializer

# Create your views here.

# viewsets通过serializer_class找到对应的serializers
class UserViewSet(viewsets.ModelViewSet):
    '''
        retrieve:
            Return a user instance.

        list:
            Return all users,ordered by most recent joined.

        create:
            Create a new user.

        delete:
            Remove a existing user.

        partial_update:
            Update one or more fields on a existing user.

        update:
            Update a user.
    '''
    queryset = User.objects.all()   # 将User的所有对象赋给queryset，并返回对应值
    serializer_class = UserSerializer   # 指向UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    '''
        retrieve:
            Return a group instance.

        list:
            Return all groups,ordered by most recent joined.

        create:
            Create a new group.

        delete:
            Remove a existing group.

        partial_update:
            Update one or more fields on a existing group.

        update:
            Update a group.
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AbstractView(View):
    form_class = Abstract
    initial = {'value': 'value'}
    tempplate_name = ''

    def get(self, requesr):
        form = self.form_class(initial=self.initial)
        return render(render, self.tempplate_name, {'form' : form})

