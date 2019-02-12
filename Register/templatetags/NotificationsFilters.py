from django import template
from Python import Hashing, init
import json
from Register.models import Users
from Articles.models import Posts
from Python.Tags import *

register = template.Library()


# GetNotification
@register.filter(name='GetNotification')
def GetNotification(Notification):
    Result = Hashing.GetAllFromHashing([
        {'Type': 'Notifications', 'Data': Notification.User_Email, 'Key': 'Email'},
        {'Type': '', 'Data': Notification.Type, 'Key': 'Type'},
        {'Type': 'Notifications', 'Data': Notification.Message, 'Key': 'Message'}])

    if Result['Result'] == -1:
        return ''

    Data = json.loads(Result['Data']['Message'])
    User = Users.objects.filter(Email=Hashing.Hash_Users(Data['Email']), Deleted=0)
    if not User.exists():
        User = ''
    else:
        Hash = Hashing.Get_Hashed_Users(User[0].Name)
        if Hash['Result'] == -1:
            User = ''
        else:
            User = Hash['Data']

    Post = Posts.objects.filter(id=Data['PostID'], Deleted=0)
    if not Post.exists():
        Title = ''
    else:
        Hash = Hashing.Get_Hashed_Articles(Post[0].ArticleTitle)
        if Hash['Result'] == -1:
            Title = ''
        else:
            Title = Hash['Data']

    User = Span(User, 'Green')
    Title = Span(Title, 'Green')
    if Result['Data']['Type'] == 1:
        Message = 'User : ' + User + ' Liked Your Post : ' + Title
    elif Result['Data']['Type'] == 2:
        Message = 'User : ' + User + ' DisLiked Your Post : ' + Title
    elif Result['Data']['Type'] == 3:
        Message = 'User : ' + User + ' Commented in Your Post : ' + Title
    else:
        Message = 'User : ' + User + ' Added New Tag in Your Post : ' + Title

    return Div(P(Message))


@register.filter(name='CheckNotifications')
def CheckNotifications(Notifications):
    return '' if len(Notifications) else Div(P('No Notifications'))


@register.filter(name='GetPicture')
def GetPicture(Notifications):
    for Notification in Notifications:
        if Notification.See == 0:
            return init.Notification
    return init.NoNotification


@register.filter(name='GetNotificationsNumber')
def GetNotificationsNumber(Notifications):
    return len(Notifications)


#################################################################################
@register.filter(name='GetTheWholeNotification')
def GetTheWholeNotification(Notification):
    Result = Hashing.GetAllFromHashing([
        {'Type': 'Notifications', 'Data': Notification.User_Email, 'Key': 'Email'},
        {'Type': '', 'Data': Notification.Type, 'Key': 'Type'},
        {'Type': 'Notifications', 'Data': Notification.Message, 'Key': 'Message'},
        {'Type': 'Date', 'Data': Notification.Date, 'Key': 'Date'}])

    if Result['Result'] == -1:
        return ''

    Data = json.loads(Result['Data']['Message'])
    Comment = Data['Comment'] if 'Comment' in Data else ''
    User = Users.objects.filter(Email=Hashing.Hash_Users(Data['Email']), Deleted=0, Activate=1)
    if not User.exists():
        UserName = ''
        UserPicture = init.OfflineUser
        UserID = ''
    else:
        Hash = Hashing.GetAllFromHashing([
            {'Type': 'Users', 'Data': User[0].Name, 'Key': 'Name'},
            {'Type': '', 'Data': User[0].id, 'Key': 'ID'},
            {'Type': 'Users', 'Data': User[0].Picture, 'Key': 'Picture'}])

        if Hash['Result'] == -1:
            UserName = ''
            UserPicture = init.OfflineUser
            UserID = ''
        else:
            UserName = Hash['Data']['Name']
            UserPicture = Hash['Data']['Picture']
            UserID = Hash['Data']['ID']

    Post = Posts.objects.filter(id=Data['PostID'], Deleted=0)
    if not Post.exists():
        Title = ''
    else:
        Hash = Hashing.Get_Hashed_Articles(Post[0].ArticleTitle)
        if Hash['Result'] == -1:
            Title = ''
        else:
            Title = Hash['Data']

    if Notification.See == 0:
        Class = 'Notification DidNotSeeNotification'
    else:
        Class = 'Notification'

    from Register.models import Notifications
    Notifications.objects.filter(id=Notification.id).update(See=1)

    Title = Strong(Title)
    if Result['Data']['Type'] == 1:
        Message = 'This User Liked Your Post : ' + Title
    elif Result['Data']['Type'] == 2:
        Message = 'This User DisLiked Your Post : ' + Title
    elif Result['Data']['Type'] == 3:
        Message = 'This User Commented in Your Post : ' + Title
    else:
        Message = 'This User Added New Tag To Your Post : ' + Title

    return Div(Div(A(init.User+str(UserID), InputImage(UserPicture)) +
                   Div(P(Strong('By : ') + UserName) +
                       P(Strong('Date : ')+Result['Data']['Date']))) +
               Div(P(Message) +
                   A(GetLink(Data['PostID'], Result['Data']['Type'], Comment),
                     'The Link For Article')
                   ), Class)


def GetLink(ID, Type, Comment):
    return init.Article + str(ID) + ('#Comment'+str(Comment) if Type == 3 or Type == 4 else '')


@register.filter(name='CheckNotificationsNumber')
def CheckNotificationsNumber(Notifications):
    if len(Notifications) < 7:
        return ''
    return Div(Input('button', 'Show More Notifications', '', '',
                     'GetMoreNotifications();'), 'Show_More_Div')
