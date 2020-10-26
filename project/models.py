from django.db import models

# Create your models here.
from abstract.models import Abstract


class Project(models.Model):

    name = models.CharField(max_length=200)

    create_date = models.DateTimeField()

    abstractID = models.IntegerField()

    autherID = models.IntegerField()










