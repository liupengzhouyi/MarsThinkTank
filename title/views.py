from rest_framework.generics import CreateAPIView, ListAPIView

from title.models import Title
from title.serializer import CreateTitleSerializer

# Create your views here.


class CreateTitle(CreateAPIView):
    """
    Create title
    """

    serializer_class = CreateTitleSerializer

class TitleList(ListAPIView):
    """
    查看所有title
    """

    queryset = Title.objects.all()
    serializer_class = CreateTitleSerializer


