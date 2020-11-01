from django.db import models

# Create your models here.

from django.db import models

class FileByLP(models.Model):

    name = models.CharField(max_length=100)

    file = models.FileField(upload_to='upload/')

