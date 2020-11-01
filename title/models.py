from django.db import models

# Create your models here.


class Title(models.Model):

    # title name
    name = models.CharField(max_length=100)

    # title created date time
    createDateTime = models.DateTimeField()

    # who create this title
    authorID = models.IntegerField()

    def toJson(self):
        return {
            'name': self.name,
            'createDateTime': self.createDateTime,
            'authorID': self.authorID
        }


