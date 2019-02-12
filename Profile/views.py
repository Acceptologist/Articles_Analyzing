from Python import init, StatusPages, URL, Hashing
from Python import GlobalFunctions as GF
from django.http import HttpResponseRedirect
from Register.models import Users, Notifications
from Articles.models import Posts
from Python.Render import __Render, Settings_Render, UserProfile_Render, MyNotifications_Render
from Python.Forms import CheckNameForm, PasswordForm, ImageForm
from django.core.files import uploadedfile


# Settings Page
def Settings(Request, Section='Picture'):
    if not GF.SESSION(Request):
        return StatusPages.UnAuthurithedUserPage(Request, 'Settings')

    if Request.method == 'POST' and URL.REFERER_is_Set(Request):

        if URL.GetURL(Request) == init.Settings:
            return Settings_PictureResponse(Request)
        elif URL.GetURL(Request) == init.Settings+'/Name':
            return Settings_NameResponse(Request)
        elif URL.GetURL(Request) == init.Settings+'/Password':
            return Settings_PasswordResponse(Request)
        elif URL.GetURL(Request) == init.Settings+'/DeActivate':
            if 'DeactivateSubmit' in Request.POST:
                return Settings_Account(Request, 1)
            return Settings_Account(Request, 0)

    return Settings_Render(Request, Section,
                           Request.GET["Result"] if 'Result' in Request.GET else '')


###################
# Name Response
def Settings_NameResponse(Request):
    Form = CheckNameForm(Request.POST)
    if Form.isValid():
        if Users.objects.filter(Name=Hashing.Hash_Users(Form.GetName())).exists():
            return Settings_Render(Request, 'Name', 'ReservedName')
        return Settings_Name_SaveData(Request, Form)
    return Settings_Render(Request, 'Name')


def Settings_Name_SaveData(Request, Form):
    User = Users.objects.filter(Email=Hashing.Hash_Users(Request.session["Email"]))[0]
    User.Name = Hashing.Hash_Users(Form.GetName())
    User.save()
    Request.session["Name"] = Form.GetName()
    return HttpResponseRedirect(init.Settings + '/Name?Result=NameDone')


###################
# Password Response
def Settings_PasswordResponse(Request):
    Form = PasswordForm(Request.POST)
    if Form.isValid():
        return Settings_Password_CheckData(Request, Form)
    return Settings_Render(Request, 'Password')


def Settings_Password_CheckData(Request, Form):
    if not Users.objects.filter(Email=Hashing.Hash_Users(Request.session["Email"]),
                                Password=Hashing.Hash_Users(Form.GetOldPassword())).exists():
        return Settings_Render(Request, 'Password', 'WrongPassword')

    User = Users.objects.filter(Email=Hashing.Hash_Users(Request.session["Email"]))[0]
    User.Password = Hashing.Hash_Users(Form.GetPassword())
    User.save()
    return HttpResponseRedirect(init.Settings + '/Password?Result=PasswordDone')


###################
def Settings_PictureResponse(Request):
    Form = ImageForm(Request.POST, Request.FILES)
    if Form.isValid():
        return Settings_Render(Request, 'Name')
    return Settings_Render(Request, 'Password')


###################
def Settings_Account(Request, Type):
    User = Users.objects.filter(Email=Hashing.Hash_Users(Request.session["Email"]))[0]
    User.Activate = '0' if Type == 1 else '1'
    User.save()
    if GF.Delete_Session(Request)['Result'] == -1:
        return StatusPages.ErrorPage(Request, 'Settings')
    return HttpResponseRedirect(init.Articles)


###################################################################################
# My Profile
def MyProfile(Request):
    if not GF.SESSION(Request):
        return StatusPages.UnAuthurithedUserPage(Request, 'My Profile')

    return __Render(Request, init.MyProfile_Template, 'My Profile',
                    A=Posts.objects.filter(User_Email=Hashing.Hash_Articles(
                        Request.session["Email"]),
                                    Deleted='0')[:5])


###################################################################################
# User
def UserProfile(Request, User_id):
    User = Users.objects.filter(id=User_id, Activate=1, Deleted=0)
    if not User.exists():
        return StatusPages.NotFoundPage(Request, 'User')

    Result = Hashing.GetAllFromHashing([{'Type': 'Users', 'Data': User[0].Email, 'Key': 'Email'}])
    if Result['Result'] == -1:
        return StatusPages.ErrorPage(Request, 'User')

    Articles = Posts.objects.filter(User_Email=Hashing.Hash_Articles(Result['Data']['Email']),
                                    Deleted=0)[:5]

    return UserProfile_Render(Request, User[0], Articles)


###################################################################################
# Notifications
def MyNotifications(Request):
    if not GF.SESSION(Request):
        return StatusPages.UnAuthurithedUserPage(Request, 'My Notifications')

    UserNotifications = Notifications.objects.filter(User_Email=Hashing.Hash_Notifications(
        Request.session["Email"]
    )).order_by('-id')[:7]
    return MyNotifications_Render(Request, UserNotifications)
