from Python import init, URL, StatusPages, Hashing, Render
from Python import GlobalFunctions as GF
from django.http import HttpResponseRedirect
from .models import Users
from Articles.models import Posts
from Python.Forms import SignUPForm, LoginForm


# Sign UP Page
def SignUP(Request):
    if GF.SESSION(Request):
        return StatusPages.LogOutPage(Request, 'Sign UP')

    if Request.method == 'POST' and URL.REFERER_is_Set(Request):
        Form = SignUPForm(Request.POST)
        if Form.isValid() and URL.GetREFERER(Request) == init.SignUP:
            return SignUP_POSTResponse(Request, Form)

    return Render.SignUP_Render(Request)


def SignUP_POSTResponse(Request, Form):
    Result = SignUP_CheckData(Form)
    if Result['Result'] != 0:
        return Render.SignUP_Render(Request, Result['Data'], Form.GetName(), Form.GetEmail())
    return SignUP_SaveData(Request, Form)


def SignUP_CheckData(Form):
    if Users.objects.filter(Name=Hashing.Hash_Users(Form.GetName())).exists():
        return GF.Returns(1, 'Name Found')
    elif Users.objects.filter(Email=Hashing.Hash_Users(Form.GetEmail())).exists():
        return GF.Returns(1, 'Email Found')
    return GF.Returns(0)


def SignUP_SaveData(Request, Form):
    User = Users(Name=Hashing.Hash_Users(Form.GetName()),
                 Email=Hashing.Hash_Users(Form.GetEmail()),
                 Password=Hashing.Hash_Users(Form.GetPassword()),
                 Picture=Hashing.Hash_Users(init.OnlineUser))
    User.save()
    User = Users.objects.filter(Email=Hashing.Hash_Users(Form.GetEmail()))
    if not User.exists():
        return StatusPages.ErrorPage(Request, 'SignUP')
    return OpenSession(Request, User[0])


###########################################################################
# Log in Page
def Login(Request):
    if GF.SESSION(Request):
        return StatusPages.LogOutPage(Request, 'Log in')

    if Request.method == 'POST' and URL.REFERER_is_Set(Request):
        Form = LoginForm(Request.POST)
        if Form.isValid() and URL.GetREFERER(Request) == init.Login:
            return Login_POSTResponse(Request, Form)

    return Render.Login_Render(Request)


def Login_POSTResponse(Request, Form):
    User = Users.objects.filter(Email=Hashing.Hash_Users(Form.GetEmail()),
                                Deleted='0')[:1]
    if User.exists():
        if User[0].Password == Hashing.Hash_Users(Form.GetPassword()):
            return OpenSession(Request, User[0])
        return Render.Login_Render(Request, 'Wrong Password', Form.GetEmail())
    return Render.Login_Render(Request, 'Email Not Found')


def OpenSession(Request, User):
    Result = Hashing.GetAllFromHashing([
        {'Type': 'Users', 'Data': User.Name, 'Key': 'Name'},
        {'Type': 'Users', 'Data': User.Email, 'Key': 'Email'},
        {'Type': '', 'Data': User.Date, 'Key': 'Date'},
        {'Type': 'Users', 'Data': User.Picture, 'Key': 'Picture'},
        {'Type': 'Users', 'Data': User.Name, 'Key': 'Name'}
    ])

    if Result['Result'] == -1:
        GF.Delete_Session(Result)
        return StatusPages.ErrorPage(Request, 'Log in')

    Request.session["ID"] = User.id
    Request.session["Name"] = Result['Data']['Name']
    Request.session["Email"] = Result['Data']['Email']
    Request.session["Date"] = str(Result['Data']['Date'])
    Request.session["Picture"] = Result['Data']['Picture']
    Request.session["Articles_Number"] = Posts.objects.filter(
        User_Email=Hashing.Hash_Articles(Request.session["Email"]),
        Deleted=0).count()

    User.Activate = '1'
    User.save()

    return HttpResponseRedirect(init.Articles)
