from Python import init, StatusPages, URL, Hashing
from .models import Posts
from django.http import HttpResponseRedirect
from Python import GlobalFunctions as GF
from Python import Render
from Python.Forms import MakeArticleForm
from .templatetags.ArticlesFilters import CheckUser
from Python.StatusPages import NotFoundPage, ErrorPage


def Articles(Request):
    return Render.__Render(Request, init.Articles_Template, init.WebSiteName,
                           A=Posts.objects.filter(Deleted='0')[:5])


#########################################################################
# Make Article
def MakeArticle(Request):
    if not GF.SESSION(Request):
        return StatusPages.UnAuthurithedUserPage(Request, 'Make Article')

    if Request.method == 'POST' and URL.REFERER_is_Set(Request):
        Form = MakeArticleForm(Request.POST)
        if Form.isValid() and URL.GetREFERER(Request) == init.MakeArticle:
            return MakeArticle_POSTResponse(Request, Form)

    Post = Posts.objects.filter(User_Email=Hashing.Hash_Articles(Request.session["Email"]),
                                Deleted=0).order_by('-id')[:1]
    if not Post.exists():
        Article_id = ''
    else:
        Article_id = Post[0].id

    if 'Done' in Request.GET:
        Result = {
            'id': Article_id,
            'GetButtonValue': 'Make New Article',
            'GetResult': 'Done',
            'GetPage': ''
        }
        return Render.MakeOrEditSuccess_Render(Request, 'Make Article', Result)

    return Render.__Render(Request, init.MakeArticle_Template, 'Make Article')


def MakeArticle_POSTResponse(Request, Form):
    Post = Posts(User_Email=Hashing.Hash_Articles(Request.session["Email"]),
                 ArticleTitle=Hashing.Hash_Articles(Form.GetTitle()),
                 Article=Hashing.Hash_Articles(Form.GetArticle()), Deleted=0,
                 Tags=Hashing.Hash_Articles(Form.GetTags()))
    Post.save()
    Request.session["Articles_Number"] += 1
    return HttpResponseRedirect(init.MakeArticle+'?Done')


#########################################################################
# Edit Article
def EditArticle(Request, Article_id):
    if not GF.SESSION(Request):
        return StatusPages.UnAuthurithedUserPage(Request, 'Edit Article')

    Post = Posts.objects.filter(User_Email=Hashing.Hash_Articles(Request.session["Email"]),
                                id=Article_id, Deleted=0)
    if not Post.exists():
        return StatusPages.NotFoundPage(Request, 'Edit Article')

    if Request.method == 'POST' and URL.REFERER_is_Set(Request):
        Form = MakeArticleForm(Request.POST)
        if Form.isValid() and URL.GetREFERER(Request) == init.EditArticle+str(Post[0].id):
            return EditArticle_POSTResponse(Form, Article_id)

    Result = Hashing.GetAllFromHashing([
        {'Type': 'Articles', 'Data': Post[0].Article, 'Key': 'Post'},
        {'Type': 'Articles', 'Data': Post[0].ArticleTitle, 'Key': 'Title'},
        {'Type': 'Articles', 'Data': Post[0].Tags, 'Key': 'Tags'}])

    if Result['Result'] == -1:
        return StatusPages.ErrorPage(Request, 'Edit Article')

    if 'Edited' in Request.GET:
        Result = {
            'id': Article_id,
            'GetButtonValue': 'Edit This Article',
            'GetResult': 'Edited',
            'GetPage': ''
        }
        return Render.MakeOrEditSuccess_Render(Request, 'Edit Article', Result)

    return Render.EditArticle_Render(Request, 'Edited' if 'Edited' in Request.GET else '',
                                     Result['Data']['Title'], Result['Data']['Post'],
                                     Result['Data']['Tags'])


def EditArticle_POSTResponse(Form, Article_id):
    Posts.objects.filter(id=Article_id).update(Article=Hashing.Hash_Articles(Form.GetArticle()),
                                               ArticleTitle=Hashing.Hash_Articles(Form.GetTitle()),
                                               Tags=Hashing.Hash_Articles(Form.GetTags()))
    return HttpResponseRedirect(init.EditArticle + str(Article_id) + '?Edited')


#########################################################################
# Show Article
def Article(Request, Article_id):
    Post = Posts.objects.filter(Deleted='0', id=Article_id)
    if not Post.exists():
        return NotFoundPage(Request, 'Article')

    Result = CheckUser(Post[0].User_Email)
    if Result['Result'] == -1:
        return ErrorPage(Request, 'Article')
    elif Result['Result'] == 0:
        return NotFoundPage(Request, 'Article')

    return Render.Article_Render(Request, Post[0])
