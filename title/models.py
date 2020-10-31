from django.db import models

# Create your models here.


class Title(models.Model):

    name = models.CharField(max_length=100)

    createDateTime = models.DateTimeField()

    authorID = models.IntegerField()



