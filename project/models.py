from django.db import models

# Create your models here.
from abstract.models import Abstract


class Project(models.Model):

    name = models.CharField(max_length=200)

    create_date = models.DateTimeField()

    autherID = models.IntegerField()

    def __str__(self):
        return 'name：%s  create_data：%d  autherI：%s' % (self.name, self.create_date, self.autherID)








