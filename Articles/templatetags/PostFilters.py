from django import template
from Python import Hashing, init
from Register.models import Users
from Articles.models import Comments, LikesDisLikes
from Python.GlobalFunctions import Returns
from Python.Tags import *
from Articles.templatetags.ArticlesFilters import CheckUser, GetText

register = template.Library()


# Article Filter
# Get Article User Data
@register.filter(name='GetUserPicture')
def GetUserPicture(Article):
    return GetUser(Article, init.OnlineUser, 'Picture')


@register.filter(name='GetUserName')
def GetUserName(Article):
    return GetUser(Article, 'UnKnown', 'Name')


@register.filter(name='GetUserLink')
def GetUserLink(Article):
    return GetUser(Article, '', 'ID')


def GetUser(Article, ErrorReturn, Key):
    Result = CheckUser(Article.User_Email)
    if Result['Result'] == -1:
        return ErrorReturn
    return init.User + str(Result['Data']['ID']) if Key == 'ID' else Result['Data'][Key]


##############################################################################
# Get Post Data
@register.filter(name='GetPostDate')
def GetPostDate(Article):
    return str(Article.Date)


@register.filter(name='GetPostTitle')
def GetPostTitle(Article):
    Result = Hashing.GetAllFromHashing([{'Type': 'Articles', 'Data': Article.ArticleTitle,
                                         'Key': 'Title'}])
    return 'UnKnown' if Result['Result'] == -1 else Result['Data']['Title']


@register.filter(name='GetArticlePost')
def GetArticlePost(Article):
    Result = Hashing.GetAllFromHashing([{'Type': 'Articles', 'Data': Article.Article,
                                         'Key': 'Article'}])
    return P('Error in Getting Post') if Result['Result'] == -1 else GetText(Result['Data']['Article'])


@register.filter(name='GetArticleTags')
def GetArticleTags(Article):

    Result = Hashing.GetAllFromHashing([{'Type': 'Articles', 'Data': Article.Tags, 'Key': 'Tags'}])
    return Span('No Tags') if Result['Result'] == -1 else GetTags(Result['Data']['Tags'])


def GetTags(Tags, List_Return=0):
    List = Tags.split('#')
    Result = ''
    The_List = []
    for Tag in List:
        if Tag != '':
            Filtered_Tag = Filter_Tag(Tag)
            if List_Return == 0:
                Result += (A('', Strong('#'+Filter_Tag(Tag)), 'Tags'))
            else:
                The_List.append(Filtered_Tag)

    if List_Return == 0:
        return Span('No Tags') if not len(Result) else Result
    else:
        return The_List


def Filter_Tag(Tag):
    List = Tag.split(' ')
    Result = []
    for i in List:
        if i != '':
            Result.append(i)

    if len(Result) <= 1:
        return Result[0]

    Tag = ''
    for i in Result:
        Tag += i + ' '
    return Tag[:len(Tag)-1]


@register.filter(name='GetPostid')
def GetPostid(Article):
    return Article.id


##############################################################################
# Get Post Statics Count
@register.filter(name='GetPostCommentsCount')
def GetPostCommentsCount(Article):
    return Comments.objects.filter(Post_id=Article.id).count()


@register.filter(name='GetPostLikes')
def GetPostLikes(Article):
    return LikesDisLikes.objects.filter(Post_id=Article.id, Status=0).count()


@register.filter(name='GetPostDisLikes')
def GetPostDisLikes(Article):
    return LikesDisLikes.objects.filter(Post_id=Article.id, Status=1).count()


##############################################################################
# Get Comments
@register.filter(name='GetPostComments')
def GetPostComments(Article):
    The_Comments = ''
    for Comment in Comments.objects.filter(Post_id=Article.id):
        Result = Filter_Comment(Comment)
        if Result['Result'] == 1:
            Comment = Result['Data']
            The_Comments += Div(
                Div(A(init.User + str(Comment['id']),
                      InputImage(Comment['Picture'])) +
                    Div(P('By : ' + Comment['Name']) +
                        P('Date : ' + Comment['Date']))) +
                Div(P(GetText(Comment['Comment'])), 'Comment_Text'),
                'Comments', 'Comment'+str(Comment['ID']))

    return The_Comments


def Filter_Comment(Comment):
    Result = Hashing.GetAllFromHashing([
        {'Type': 'Comments', 'Data': Comment.User_Email, 'Key': 'Email'},
        {'Type': 'Comments', 'Data': Comment.Comment, 'Key': 'Comment'},
        {'Type': 'Date', 'Data': Comment.Date, 'Key': 'Date'},
        {'Type': '', 'Data': Comment.id, 'Key': 'ID'}])

    if Result['Result'] == -1:
        return Returns(-1, 'Searching For User', Result['Error'])

    User = Users.objects.filter(Email=Hashing.Hash_Users(Result['Data']['Email']),
                                Deleted='0', Activate='1')
    if not User.exists():
        return Returns(0, 'Not Found')

    Filtered_Comment = Result['Data']

    Result = Hashing.GetAllFromHashing([
        {'Type': 'Users', 'Data': User[0].Name, 'Key': 'Name'},
        {'Type': 'Users', 'Data': User[0].Picture, 'Key': 'Picture'},
        {'Type': '', 'Data': User[0].id, 'Key': 'id'}])

    if Result['Result'] == -1:
        return Returns(-1, 'Getting User Name From Hashing')

    Filtered_Comment['Name'] = Result['Data']['Name']
    Filtered_Comment['Picture'] = Result['Data']['Picture']
    Filtered_Comment['id'] = Result['Data']['id']

    return Returns(1, Filtered_Comment)
