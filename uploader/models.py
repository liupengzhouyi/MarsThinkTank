
from django.db import models
from django.utils import timezone

# Create your models here.


'''
文件记录
'''

class FileInfo(models.Model):

    file_name = models.CharField(max_length=150)

    file_ne_name = models.CharField(max_length=200)

    file_size = models.DecimalField(max_digits=10, decimal_places=0)

    file_path = models.CharField(max_length=500)

    upload_time = models.DateTimeField()

    authorID = models.IntegerField()


