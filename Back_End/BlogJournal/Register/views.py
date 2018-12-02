from django.shortcuts import render
from Python import init, URL, PagesStatus, Hashing, GlobalFunctions
from django.http import HttpResponseRedirect
from Register.models import Users
from Blogs.models import Posts


# Sign UP Page
def SignUP(Request):
    if 'Name' in Request.session:
        return PagesStatus.LogOutPage(Request, 'Sign UP')

    if Request.method == 'POST' and 'N' in Request.POST and (
            'E' in Request.POST and 'P' in Request.POST and (
            Request.META["HTTP_REFERER"] is not None)):
        return SignUP_POSTResponse(Request)

    return Render(Request, 'Register/SignUP.html', 'Sign UP', '', '', '')


def SignUP_POSTResponse(Request):
    if URL.GetURL(Request) == init.SignUP:
        Result = SignUP_CheckData(Request)
        if Result != 'Not Found':
            if Result != 'Found':
                return Render(Request, 'Register/SignUP.html', 'Sign UP', '', '', '')
            return Render(Request, 'Register/SignUP.html', 'Sign UP', 'Found',
                          Request.POST["N"], Request.POST["E"])
        else:
            return SignUP_SaveData(Request)
    else:
        return PagesStatus.UnAuthurithedUserPage(Request, 'Sign UP')


def SignUP_CheckData(Request):
    Result = GlobalFunctions.Check_Len(Request.POST["N"], init.Name_Len)
    if Result != 'OK':
        return Result

    Result = GlobalFunctions.Check_Len(Request.POST["E"], init.Email_Len)
    if Result != 'OK':
        return Result

    Result = GlobalFunctions.Check_Len(Request.POST["P"], init.Password_Len)
    if Result != 'OK':
        return Result

    try:
        Users.objects.get(Email=Hashing.Hash_Users(Request.POST["E"]))
    except Users.DoesNotExist:
        return 'Not Found'
    else:
        return 'Found'


def SignUP_SaveData(Request):
    User = Users(Name=Hashing.Hash_Users(Request.POST["N"]),
                 Email=Hashing.Hash_Users(Request.POST["E"]),
                 Password=Hashing.Hash_Users(Request.POST["P"]),
                 Picture=Hashing.Hash_Users(init.ProfilePicture))
    User.save()
    return OpenSession(Request, 'Register/SignUP.html', 'Sign UP', User)


###########################################################################
# Log in Page
def Login(Request):
    if 'Name' in Request.session:
        return PagesStatus.LogOutPage(Request, 'Log in')

    if Request.method == 'POST' and 'E' in Request.POST and (
      'P' in Request.POST and Request.META["HTTP_REFERER"] is not None):
        return Login_POSTResponse(Request)

    return Render(Request, 'Register/Login.html', 'Log in', '', '', '')


def Login_POSTResponse(Request):
    if URL.GetURL(Request) == init.Login:
        [Result, User] = Login_CheckData(Request)
        if Result != 'OK':
            return Render(Request, 'Register/Login.html', 'Log in', Result, '', Request.POST["E"])
        else:
            return OpenSession(Request, 'Register/Login.html', 'Log in', User)
    else:
        return PagesStatus.UnAuthurithedUserPage(Request, 'Sign UP')


def Login_CheckData(Request):
    try:
        User = Users.objects.get(Email=Hashing.Hash_Users(Request.POST["E"]))
    except Users.DoesNotExist:
        return ['Not Found', '']
    else:
        if User.Password == Hashing.Hash_Users(Request.POST["P"]):
            return ['OK', User]
        return ['Wrong Password', '']


############################################################################
# Open Session
def OpenSession(Request, Page, Title, User):
    # Name
    [Result, Value] = Hashing.Get_Hashed_Users(User.Name)
    if Result == -1:
        return Render(Request, Page, Title, 'Error in Opening Session', '', '')
    Request.session["Name"] = Value

    # Email
    [Result, Value] = Hashing.Get_Hashed_Users(User.Email)
    if Result == -1:
        GlobalFunctions.Delete_Session(Request)
        return Render(Request, Page, Title, 'Error in Opening Session', '', '')
    Request.session["Email"] = Value

    # Date
    Request.session["Date"] = str(User.Date)

    # Profile Picture
    [Result, Value] = Hashing.Get_Hashed_Users(User.Picture)
    if Result == -1:
        GlobalFunctions.Delete_Session(Request)
        return Render(Request, Page, Title, 'Error in Opening Session', '', '')
    Request.session["Picture"] = Value

    # Blogs Number
    Request.session["Blogs_Number"] = Posts.objects.filter(
        User_Email=Hashing.Hash_Posts(Request.session["Email"])).count()
    return HttpResponseRedirect(init.Main)


def Render(Request, Page, Title, Wrong, Name, Email):
    return render(Request, Page, {
        'init': init,
        'Title': Title,
        'Wrong': Wrong,
        'Name': Name,
        'Email': Email,
        'Ajax_API': init.Errors[0]['API'],
        'Ajax_Message': init.Errors[0]['Message'],
        'JSON_API': init.Errors[1]['API'],
        'JSON_Message': init.Errors[1]['Message']
    })
