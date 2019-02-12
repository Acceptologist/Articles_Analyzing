from django.db import models
from Python import init


class Posts(models.Model):
    User_Email = models.CharField(max_length=init.Email_Len)
    ArticleTitle = models.CharField(max_length=init.ArticleTitle_Len)
    Article = models.CharField(max_length=init.Article_Len)
    Tags = models.CharField(max_length=init.ArticleTags_Len, default='')
    Deleted = models.BooleanField()
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'User Email Who Write The Post : ' + str(self.User_Email)


class LikesDisLikes(models.Model):
    User_Email = models.CharField(max_length=110)
    Post_id = models.CharField(max_length=11)
    Status = models.BooleanField()
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'User : ' + str(self.User_Email) + ' Like Or DisLike Post : ' + str(self.Post_id)


class Comments(models.Model):
    Post_id = models.IntegerField()
    User_Email = models.CharField(max_length=init.Email_Len)
    Comment = models.CharField(max_length=init.Comment_Len)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'User : ' + str(self.User_Email) + ' Comment in Post : ' + str(self.Post_id)
