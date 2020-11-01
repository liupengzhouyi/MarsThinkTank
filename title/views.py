from requests import Response
from rest_framework.generics import CreateAPIView, ListAPIView

from title.models import Title
from title.serializer import CreateTitleSerializer

# Create your views here.


class BaseResponse(object):
    """
    初始化基本的返回数据信息
    """
    def __init__(self,status=True,data=None,error=None):
        self.status = status
        self.data = data
        self.error = error

    @property
    def get_data(self):
        return self.__dict__

class CreateTitle(CreateAPIView):
    """
    Create title
    """

    serializer_class = CreateTitleSerializer

    def get(self, Title):
        ret = BaseResponse()
        ret.data = 123
        return Response(ret.get_data)
    

class TitleList(ListAPIView):
    """
    查看所有title
    """

    queryset = Title.objects.all()
    serializer_class = CreateTitleSerializer


