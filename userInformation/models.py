from django.db import models

# Create your models here.


class UserInformation(models.Model):
    '''user information'''

    # 名称
    name = models.CharField(max_length=40)

    # E-mail
    email = models.CharField(max_length=80)

    # phone number
    phoneNumber = models.CharField(max_length=15)

    # password
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def toJson(self):
        return {'name': self.name, 'email': self.email, 'phoneNumber': self.phoneNumber, 'password': self.password}

