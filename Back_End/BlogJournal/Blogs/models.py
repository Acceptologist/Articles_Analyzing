from django.db import models


class Posts(models.Model):
    User_Email = models.CharField(max_length=110)
    Post = models.CharField(max_length=2050)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'User id Who Write The Post : ' + self.User_id
