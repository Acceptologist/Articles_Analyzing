from django.shortcuts import render
from Python import init
from Python.GlobalFunctions import SESSION
from Register.models import Notifications
from Python import Hashing


# R = Request, Template = Page Template, T = Title, W = Wrong, N = Name, E = Email, R = Result
# A = Articles, P = Post, S = Section, U = User, T = Article_Title, UN = UserNotifications
# Tags = Article Tags
def __Render(Request, Template, Title, W='', N='', E='', A='', P='', R='', S='', U='', T='',
             UN='', Tags=''):
    Session = GetSession(Request)
    The_Notifications = GetNotifications(Request)

    return render(Request, Template, {
        # 'Session': GetSession(Request),

        'Session': Session['Session'],
        'Session_ID': Session['ID'],
        'Session_Name': Session['Name'],
        'Session_Picture': Session['Picture'],
        'Session_Articles_Number': Session['Articles_Number'],
        'Session_Email': Session['Email'],
        'Session_Date': Session['Date'],

        'Notifications': The_Notifications,
        'User_Notifications': UN,

        'init': init,
        'Title': Title,

        'Wrong': W,
        'Name': N,
        'Email': E,

        'Articles': A,
        'Post': P,
        'Article_Title': T,
        'Tags': Tags,

        'Result': R,

        'Section': S,

        'User': U
    })


def GetSession(Request):
    Session = {
        'Session': '',
        'ID': '',
        'Name': '',
        'Email': '',
        'Picture': init.OfflineUser,
        'Articles_Number': '',
        'Date': ''}
    if SESSION(Request):
        Session['Session'] = 'Found'
        Session['ID'] = Request.session["ID"]
        Session['Name'] = Request.session["Name"]
        Session['Email'] = Request.session['Email']
        Session['Picture'] = Request.session["Picture"]
        Session['Articles_Number'] = Request.session["Articles_Number"]
        Session['Date'] = Request.session['Date']
    return Session


def GetNotifications(Request):
    if not SESSION(Request):
        return ''
    return Notifications.objects.filter(User_Email=Hashing.Hash_Notifications(
        Request.session["Email"]
    )).order_by('-id')[:3]


# Render Functions
##########################
# Register
def SignUP_Render(Request, Wrong='', Name='', Email=''):
    return __Render(Request, init.SignUP_Template, 'Sign UP', W=Wrong, N=Name, E=Email)


def Login_Render(Request, Wrong='', Email=''):
    return __Render(Request, init.Login_Template, 'Log in', W=Wrong, E=Email)


##########################
# Articles
def EditArticle_Render(Request, Result, Title, Post, Tags):
    return __Render(Request, init.EditArticle_Template, 'Edit Article', R=Result, P=Post,
                    T=Title, Tags=Tags)


def MakeOrEditSuccess_Render(Request, Title, Result):
    return __Render(Request, init.MakeOrEditSuccess_Template, Title, R=Result)


def Article_Render(Request, Post):
    return __Render(Request, init.Article_Template, 'Article', P=Post)


##########################
# Profile
def Settings_Render(Request, Section, Result=''):
    return __Render(Request, init.Settings_Template, 'Settings', S=Section, R=Result)


def UserProfile_Render(Request, User, Articles):
    return __Render(Request, init.User_Template, 'User', U=User, A=Articles)


def MyNotifications_Render(Request, UserNotifications):
    return __Render(Request, init.Notifications_Template, 'My Notifications', UN=UserNotifications)
