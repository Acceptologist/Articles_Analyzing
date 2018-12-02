from django.shortcuts import render
from Python import init, PagesStatus, URL, GlobalFunctions, Hashing
from .models import Posts
from django.http import HttpResponse


def Main(Request):
    if 'Name' in Request.session:
        Session = 'Found'
        Session_Name = Request.session["Name"]
    else:
        Session = 'NO'
        Session_Name = ''

    return render(Request, 'Blogs/Main.html', {
        'init': init,
        'Title': init.WebSiteName,
        'Session': Session,
        'Session_Name': Session_Name
    })


#########################################################################
# Make Blog
def MakeBlog(Request):
    if 'Name' not in Request.session:
        return PagesStatus.UnAuthurithedUserPage(Request, 'Make Blog')

    if Request.method == 'POST' and 'B' in Request.POST and Request.META["HTTP_REFERER"] is not None:
        return MakeBlog_POSTResponse(Request)

    return render(Request, 'Blogs/Make_Blog.html', {
        'init': init,
        'Title': 'Make Blog',
        'Session_Name': Request.session["Name"]
    })


def MakeBlog_POSTResponse(Request):
    if URL.GetURL(Request) == init.MakeBlog:
        Result = MakeBlog_CheckData(Request)
        if Result != 'OK':
            return render(Request, 'Blogs/Make_Blog.html', {
                'init': init,
                'Title': 'Make Blog',
                'Session_Name': Request.session["Name"]
            })
        else:
            MakeBlog_SaveData(Request)
            return HttpResponse('Post Saved')
    else:
        return PagesStatus.UnAuthurithedUserPage(Request, 'Make Blog')


def MakeBlog_CheckData(Request):
    return GlobalFunctions.Check_Len(Request.POST["B"], init.Blog_Len)


def MakeBlog_SaveData(Request):
    Post = Posts(User_Email=Hashing.Hash_Posts(Request.session["Email"]),
                 Post=Hashing.Hash_Posts(Request.POST["B"]))
    Post.save()
    pass
