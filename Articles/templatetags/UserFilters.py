from django import template
from Python import Hashing
from Python.init import OnlineUser
from Articles.models import Posts, LikesDisLikes, Comments

register = template.Library()


############################################################################################
# User in Article
@register.filter(name='GetUserPicture')
def GetUserPicture(User):
    Result = Hashing.GetAllFromHashing([{'Type': 'Users', 'Data': User.Picture, 'Key': 'Picture'}])
    return OnlineUser if Result['Result'] == -1 else Result['Data']['Picture']


@register.filter(name='GetUserID')
def GetUserID(User):
    return str(User.id)


@register.filter(name='GetUserName')
def GetUserName(User):
    Result = Hashing.GetAllFromHashing([{'Type': 'Users', 'Data': User.Name, 'Key': 'Name'}])
    return 'UnKnown' if Result['Result'] == -1 else Result['Data']['Name']


@register.filter(name='GetUserLikes')
def GetUserLikes(User):
    Result = Hashing.GetAllFromHashing([{'Type': 'Users', 'Data': User.Email, 'Key': 'Email'}])
    if Result['Result'] == -1:
        return '0'
    return LikesDisLikes.objects.filter(User_Email=Hashing.Hash_LikeDisLike(
        Result['Data']['Email']), Status=0).count()


@register.filter(name='GetUserDisLikes')
def GetUserDisLikes(User):
    Result = Hashing.GetAllFromHashing([{'Type': 'Users', 'Data': User.Email, 'Key': 'Email'}])
    if Result['Result'] == -1:
        return '0'
    return LikesDisLikes.objects.filter(User_Email=Hashing.Hash_LikeDisLike(
        Result['Data']['Email']), Status=1).count()


@register.filter(name='GetUserComments')
def GetUserComments(User):
    Result = Hashing.GetAllFromHashing([{'Type': 'Users', 'Data': User.Email, 'Key': 'Email'}])
    if Result['Result'] == -1:
        return '0'
    return Comments.objects.filter(
        User_Email=Hashing.Hash_Comments(Result['Data']['Email'])).count()


@register.filter(name='GetUserArticlesNumber')
def GetUserArticlesNumber(User):
    Result = Hashing.GetAllFromHashing([{'Type': 'Users', 'Data': User.Email, 'Key': 'Email'}])
    if Result['Result'] == -1:
        return 'UnKnown'
    return Posts.objects.filter(User_Email=Hashing.Hash_Articles(Result['Data']['Email']),
                                Deleted=0).count()


############################################################################################
# User in Profile
@register.filter(name='GetLikes')
def GetLikes(User_Email):
    return LikesDisLikes.objects.filter(User_Email=Hashing.Hash_LikeDisLike(User_Email),
                                        Status=0).count()


@register.filter(name='GetDisLikes')
def GetDisLikes(User_Email):
    return LikesDisLikes.objects.filter(User_Email=Hashing.Hash_LikeDisLike(User_Email),
                                        Status=1).count()


@register.filter(name='GetComments')
def GetComments(User_Email):
    return Comments.objects.filter(User_Email=Hashing.Hash_Comments(User_Email)).count()
