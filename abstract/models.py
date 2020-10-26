from django.db import models

# Create your models here.

class Abstract(models.Model):
    '''Abstract Information Class'''

    # Abstract type (project, title, direction, demonstration)
    abstractType = models.IntegerField()

    # This abstract for which one?
    fatherID = models.IntegerField()

    # Abstract file type (PDF, DOC, DOCX, MD, HTML)
    abstractFileType = models.IntegerField()

    # Abstract download link
    downloadLink = models.CharField(max_length=250)

    abstract = models.CharField(max_length=250)

