from django import template
from Python import Hashing, init
from Register.models import Users
from Articles.models import LikesDisLikes, Comments
from Python.GlobalFunctions import Returns
from Python.Tags import *


register = template.Library()


# Articles
@register.filter(name='GetPost')
def GetPost(Article, args='0'):
    Result = CheckUser(Article.User_Email)
    if Result['Result'] != 1:
        return ''

    Result = Hashing.GetAllFromHashing([
        {'Type': 'Articles', 'Data': Article.ArticleTitle, 'Key': 'Title'},
        {'Type': 'Articles', 'Data': Article.Article, 'Key': 'Article'},
        {'Type': 'Articles', 'Data': Article.Tags, 'Key': 'Tags'},
        {'Type': 'Date', 'Data': Article.Date, 'Key': 'Date'},
        {'Type': '', 'Data': Result['Data']['Name'], 'Key': 'Name'},
        {'Type': '', 'Data': Result['Data']['Picture'], 'Key': 'Picture'},
        {'Type': '', 'Data': Result['Data']['ID'], 'Key': 'ID'}])

    if Result['Result'] == -1:
        return ''

    Likes = LikesDisLikes.objects.filter(Post_id=Article.id, Status=0).count()
    DisLikes = LikesDisLikes.objects.filter(Post_id=Article.id, Status=1).count()
    CommentsCount = Comments.objects.filter(Post_id=Article.id).count()

    return Div(
        Div(Div(A(init.User + str(Result['Data']['ID']), InputImage(init.OnlineUser))) +
            Div(P(Strong('By ') + ' : ' + Result['Data']['Name']) +
                P(Strong('Date ') + ' : ' + Result['Data']['Date'])) +
            GetOptions(str(Article.id), args), 'Article_Header') +
        P(Strong('Title : ') + Result['Data']['Title'], 'Article_Title') +
        P(
            Strong('Tags : ') +
            GetArticleTags(Result['Data']['Tags']), 'Article_Tags'
        ) +
        Div(P(GetText(Result['Data']['Article'], 2))) +
        Div(A(init.Article + str(Article.id), 'The Link To Full Article'), 'Article_Link') +
        Div(P(Span('Likes ') + str(Likes)) +
            P(Span('DisLikes ') + str(DisLikes)) +
            P(Span('Comments ') + str(CommentsCount)), 'Article_Statics'),
        'Article', 'Post'+str(Article.id))


def GetArticleTags(Tags):
    from Articles.templatetags.PostFilters import GetTags
    return GetTags(Tags)


def GetOptions(ID, Option):
    return '' if Option != '1' else Div(InputImage(init.DropDown, '', 'MakeSlide(' + ID + ');') +
                                        Div(A('', 'Edit', '', 'Edit(' + ID + ')') +
                                            A('', 'Delete', 'Delete', 'Delete(' + ID + ')'),
                                            '', 'DropDownBox' + ID), 'Options')


def CheckUser(Email):
    Result = Hashing.GetAllFromHashing([{'Type': 'Articles', 'Data': Email, 'Key': 'Email'}])
    if Result['Result'] == -1:
        return Returns(-1, 'Searching For User', Result['Error'])

    User = Users.objects.filter(Email=Hashing.Hash_Users(Result['Data']['Email']),
                                Deleted='0', Activate='1')
    if not User.exists():
        return Returns(0, 'Not Found')

    Result = Hashing.GetAllFromHashing([
        {'Type': 'Users', 'Data': User[0].Name, 'Key': 'Name'},
        {'Type': 'Users', 'Data': User[0].Picture, 'Key': 'Picture'},
        {'Type': '', 'Data': User[0].id, 'Key': 'ID'},
        {'Type': '', 'Data': Result['Data']['Email'], 'Key': 'Email'}])

    if Result['Result'] == -1:
        return Returns(-1, 'Searching For User', Result['Error'])

    return Returns(1, Result['Data'])


def GetText(Article, CountUntil=-1):
    Count = 0
    Text = ''
    for i in range(len(Article)):
        if Article[i] == '\n':
            Count += 1
            Text += '</p><p>'
        else:
            Text += Article[i]

        if CountUntil != -1:
            if Count == CountUntil:
                return Text
    return Text


# Check Posts Number To Put Text
@register.filter(name='CheckPostsNumber')
def CheckPostsNumber(Articles):
    if not len(Articles):
        return P('No Posts Was Found', 'Not_Found_Text')
    elif len(Articles) < 5:
        return ''
    return Div(Input('button', 'Show More', '', '', 'GetMorePosts();'), 'Show_More_Div')
