from django.db import models


class Users(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=110)
    Password = models.CharField(max_length=50)
    Picture = models.CharField(max_length=110, default='None')
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'The User is : ' + str(self.Name)
