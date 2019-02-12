from django.db import models
from Python import init


class Users(models.Model):
    Name = models.CharField(max_length=init.Name_Len, default='None')
    Deleted = models.BooleanField(default=0)
    Activate = models.BooleanField(default=1)
    Email = models.CharField(max_length=init.Email_Len, default='None')
    Password = models.CharField(max_length=init.Password_Len, default='None')
    Picture = models.CharField(max_length=init.Picture_Len, default='None')
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'The User is : ' + str(self.Name)


class Notifications(models.Model):
    User_Email = models.CharField(max_length=init.Email_Len, default='None')
    See = models.BooleanField(default=0)
    Type = models.IntegerField()
    Message = models.CharField(max_length=init.NotificationsMessage_Len)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'The User : ' + str(self.User_Email) + ' Have Received Notification'
