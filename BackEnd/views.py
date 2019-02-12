import json
import re
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from Articles.models import Posts, Comments, LikesDisLikes
from Articles.templatetags import ArticlesFilters as ASF
from Python import GlobalFunctions as GF
from Python import Hashing, init, StatusPages, URL
from Python.Forms import CheckNameForm, CheckEmailForm, CheckPostsNumberForm, MakeCommentForm, \
    LikeDisLikeForm
from Register.models import Users, Notifications
from Python.Tags import *
from Articles.templatetags.ArticlesFilters import GetText
from Register.templatetags.NotificationsFilters import GetTheWholeNotification


def CheckName(Request):
    Form = CheckNameForm(Request.POST)
    if Form.isValid() and URL.REFERER_is_Set(Request):
        if URL.GetREFERER(Request) == init.SignUP or \
                URL.GetREFERER(Request) == init.Settings+ '/Name':
            if Users.objects.filter(Name=Hashing.Hash_Users(Form.GetName())).exists():
                return JsonResponse(GF.Returns('1'))
            return JsonResponse(GF.Returns('0'))
    return StatusPages.UnAuthurithedUserPage(Request, 'Un Authorized User')


def CheckEmail(Request):
    Form = CheckEmailForm(Request.POST)
    if Form.isValid() and URL.REFERER_is_Set(Request):
        if URL.GetREFERER(Request) == init.SignUP:
            if Users.objects.filter(Email=Hashing.Hash_Users(Form.GetEmail())).exists():
                return JsonResponse(GF.Returns('1'))
            return JsonResponse(GF.Returns('0'))
    return StatusPages.UnAuthurithedUserPage(Request, 'Un Authorized User')


def LogOut(Request):
    if GF.Delete_Session(Request)['Result'] == -1:
        return StatusPages.ErrorPage(Request, 'Log Out')
    return HttpResponseRedirect(init.Articles)


def GetPosts(Request):
    Form = CheckPostsNumberForm(Request.POST)
    if not Form.isValid():
        return JsonResponse(GF.Returns(-1, 'Not Valid Number'))

    Options = '0'
    Articles = ''
    index = int(Form.GetNumber())
    Slice = slice(index, index + 5)

    if URL.REFERER_is_Set(Request):

        if URL.GetREFERER(Request) == init.Articles+ '/':
            Options = '0'
            Articles = Posts.objects.filter(Deleted=0)[Slice]

        elif URL.GetREFERER(Request) == init.MyProfile:
            Options = '1'
            Articles = Posts.objects.filter(User_Email=Hashing.Hash_Articles(
                Request.session["Email"]), Deleted=0)[Slice]
        else:
            Match = re.search(r'' + init.User + '(\d)+', URL.GetREFERER(Request))
            if not Match:
                return StatusPages.UnAuthurithedUserPage(Request, 'Un Authorized User')
            User = Users.objects.filter(id=Match.group(1))
            if not User.exists():
                return StatusPages.UnAuthurithedUserPage(Request, 'Un Authorized User')
            Result = Hashing.GetAllFromHashing([{
                'Type': 'Users', 'Data': User[0].Email, 'Key': 'Email'}])
            if Result['Result'] == -1:
                return GF.Returns(-1, 'Getting Data From Hashing', Result['Result']['Error'])

            Articles = Posts.objects.filter(User_Email=Hashing.Hash_Articles(
                Result['Data']['Email']), Deleted=0)[Slice]
            Options = '2'

    if not Articles.exists():
        return JsonResponse(GF.Returns(0, 'No Data'))

    Result = GF.Returns(1, {
        'Posts': {},
        'Count': 0
    })
    Count = 0

    for Article in Articles:
        Text = ASF.GetPost(Article, Options)
        if Text != '':
            Count += 1
            Result['Data']['Posts'][str(Count)] = Text

    Result['Data']['Count'] = Count
    return JsonResponse(Result)


def MakeComment(Request):
    Form = MakeCommentForm(Request.POST)
    Result = CheckPost(Request, Form)

    if Result['Result'] != 1:
        if Result['Data'] == 'Not Valid':
            return StatusPages.UnAuthurithedUserPage(Request, 'Un Authorized User')
        return JsonResponse(Result)

    Comment = Comments(Post_id=Form.GetID(),
                       User_Email=Hashing.Hash_Comments(Request.session["Email"]),
                       Comment=Hashing.Hash_Comments(Form.GetComment()))
    Comment.save()
    Comment = Comments.objects.filter().order_by('-id')[:1]
    if not Comment.exists():
        Comment = ''
    else:
        Comment = Comment[0].id

    if Request.session["Email"] != Result['Data']['Email']:
        Notification = Notifications(Type=3,
                                     User_Email=Hashing.Hash_Notifications(
                                         Result['Data']['Email']),
                                     Message=Hashing.Hash_Notifications(
                                         json.dumps({
                                             'Email': Request.session["Email"],
                                             'PostID': Form.GetID(),
                                             'Comment': Comment
                                         })
                                     ))
        Notification.save()

    return JsonResponse(GF.Returns(1, Div(
        Div(A(init.User+str(Request.session["ID"]), InputImage(Request.session["Picture"])) +
            Div(P('By : '+Request.session["Name"]) +
                P('Date : '+str(datetime.datetime.now())))) +
        Div(P(GetText(Form.GetComment())), 'Comment_Text')
        , 'Comments')))


def Like_DisLikePost(Request):
    Form = LikeDisLikeForm(Request.POST)
    Result = CheckPost(Request, Form)

    if Result['Result'] != 1:
        if Result['Data'] == 'Not Valid':
            return StatusPages.UnAuthurithedUserPage(Request, 'Un Authorized User')
        return JsonResponse(Result)

    Post_Like_DisLike = LikesDisLikes.objects.filter(Post_id=Form.GetID(),
                                                     User_Email=Hashing.Hash_LikeDisLike(
                                                         Request.session["Email"]))
    if Post_Like_DisLike.exists():
        return JsonResponse(GF.Returns(0, 'You Already ' +
                                       ('Liked' if Post_Like_DisLike[0].Status == 0 else 'DisLiked')))

    LikeOrDisLike = LikesDisLikes(Post_id=Form.GetID(),
                                  User_Email=Hashing.Hash_LikeDisLike(Request.session["Email"]),
                                  Status=Form.GetType())
    LikeOrDisLike.save()

    if Request.session["Email"] != Result['Data']['Email']:
        Notification = Notifications(Type=(Form.GetType()+1),
                                     User_Email=Hashing.Hash_Notifications(
                                         Result['Data']['Email']),
                                     Message=Hashing.Hash_Notifications(
                                         json.dumps({
                                             'Email': Request.session["Email"],
                                             'PostID': Form.GetID()
                                         })
                                     ))
        Notification.save()
    return JsonResponse(GF.Returns(1, 'Done'))


def CheckPost(Request, Form):
    if not Form.isValid() or not GF.SESSION(Request) or not URL.REFERER_is_Set(Request):
        return GF.Returns(-1, 'Not Valid')

    if not URL.GetREFERER(Request) == init.Article + str(Form.GetID()):
        return GF.Returns(-1, 'Not Valid')

    Post = Posts.objects.filter(Deleted='0', id=Form.GetID())
    if not Post.exists():
        return GF.Returns(0, 'Post Not Found')

    if ASF.CheckUser(Post[0].User_Email)['Result'] != 1:
        return GF.Returns(0, 'Post Not Found')

    Result = Hashing.GetAllFromHashing([{'Type': 'Articles', 'Data': Post[0].User_Email,
                                         'Key': 'Email'}])
    if Result['Result'] == -1:
        return GF.Returns(-1, 'Searching For User', Result['Error'])

    return GF.Returns(1, Result['Data'])


def DeletePost(Request):
    Form = CheckPostsNumberForm(Request.POST)
    if not Form.isValid() or not URL.REFERER_is_Set(Request) or not GF.SESSION(Request):
        return StatusPages.UnAuthurithedUserPage(Request, 'Un Authorized User')

    if URL.GetREFERER(Request) != init.MyProfile:
        return StatusPages.UnAuthurithedUserPage(Request, 'Un Authorized User')

    if not Posts.objects.filter(User_Email=Hashing.Hash_Articles(Request.session["Email"]),
                                Deleted=0, id=Form.GetNumber()).exists():
        return JsonResponse(GF.Returns(0, 'Post Not Found'))

    Posts.objects.filter(User_Email=Hashing.Hash_Articles(Request.session["Email"]),
                         id=Form.GetNumber()).update(Deleted=1)

    Request.session["Articles_Number"] -= 1
    return JsonResponse(GF.Returns(1, 'Deleted'))


def GetMoreNotifications(Request):
    if not GF.SESSION(Request) or not URL.REFERER_is_Set(Request):
        return StatusPages.UnAuthurithedUserPage(Request, 'Un Authorized User')

    if URL.GetREFERER(Request) != init.Notifications:
        return StatusPages.UnAuthurithedUserPage(Request, 'Un Authorized User')

    Form = CheckPostsNumberForm(Request.POST)
    if not Form.isValid():
        return JsonResponse(GF.Returns(-1, 'Not Valid Number'))

    index = int(Form.GetNumber())
    Slice = slice(index, index + 7)
    The_Notifications = Notifications.objects.filter(User_Email=Hashing.Hash_Notifications(
        Request.session["Email"])).order_by('-id')[Slice]

    if not len(The_Notifications):
        return JsonResponse(GF.Returns(0, 'No Data'))

    Result = GF.Returns(1, {
        'Notifications': {},
        'Count': 0
    })
    Count = 0

    for Notification in The_Notifications:
        Text = GetTheWholeNotification(Notification)
        if Text != '':
            Count += 1
            Result['Data']['Notifications'][str(Count)] = Text

    Result['Data']['Count'] = Count
    return JsonResponse(Result)
