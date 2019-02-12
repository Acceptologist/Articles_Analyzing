# WebSite Name
WebSiteName = 'Articles Journal'


######################################################################################
# Pages
__HOST = 'http://127.0.0.1:8000'


#############
# Register
SignUP = __HOST + '/Register/SignUP'
SignUP_Template = 'Register/SignUP.html'

Login = __HOST + '/Register/Login'
Login_Template = 'Register/Login.html'


#############
# Articles
Articles = __HOST
Articles_Template = 'Articles/Articles.html'

MakeArticle = __HOST + '/Articles/MakeArticle'
MakeArticle_Template = 'Articles/MakeArticle.html'

EditArticle = __HOST + '/Articles/EditArticle/'
EditArticle_Template = 'Articles/EditArticle.html'

MakeOrEditSuccess_Template = 'Articles/MakeOrEditSuccess.HTML'

Article = __HOST + '/Articles/Article/'
Article_Template = 'Articles/Article.html'


#############
# Profile
Settings = __HOST + '/Profile/Settings'
Settings_Template = 'Profile/Settings/Settings.html'
Settings_Name_Template = 'Profile/Settings/Name.html'
Settings_Password_Template = 'Profile/Settings/Password.html'
Settings_Picture_Template = 'Profile/Settings/Picture.html'
Settings_DeActivate_Template = 'Profile/Settings/DeActivate.html'


MyProfile = __HOST + '/Profile/MyProfile'
MyProfile_Template = 'Profile/MyProfile.HTML'


User = __HOST + '/Profile/User/'
User_Template = 'Profile/User.HTML'


Notifications = __HOST + '/Profile/MyNotifications'
Notifications_Template = 'Profile/MyNotifications.HTML'


#############
# Services
Help = __HOST + '/Services/Help'
Help_Template = 'Services/Help.html'

Policy = __HOST + '/Services/Policy'
Policy_Template = 'Services/Policy.html'

######################################################################################
# Status Pages
__StatusPages = 'StatusPages/'

UnAuthurithedUserPage = __StatusPages + 'UnAuthurithedUserPage.HTML'
ErrorPage = __StatusPages + 'ErrorPage.HTML'
LogOutPage = __StatusPages + 'LogOutPage.HTML'
NotFoundPage = __StatusPages + '404.HTML'

######################################################################################
# Messages
MessageBox = 'MessageBoxs/MessageBox.html'

######################################################################################
# Picture Folder
__Pictures = 'Pictures/'

# Main Pictures
LOGO = __Pictures + 'LOGO.JPG'
OnlineUser = __Pictures + 'OnlineUser.PNG'
OfflineUser = __Pictures + 'OfflineUser.PNG'
AddPicture = __Pictures + 'AddPicture.PNG'
NoNotification = __Pictures + 'NoNotification.PNG'
Notification = __Pictures + 'Notification.PNG'
Send = __Pictures + 'Send.PNG'
DropDown = __Pictures + 'DropDown.PNG'


######################################################################################
# Length
# Sign UP
Name_Len = 40
Email_Len = 100
Password_Len = 40
Picture_Len = 40

# Make Article
Article_Len = 2000
ArticleTitle_Len = 50
ArticleTags_Len = 100

# Articles
id_Len = 15

# Settings
Picture_Byte_Len = 2097152


# Article
Comment_Len = 500

# Notifications
NotificationsType_Len = 1
NotificationsMessage_Len = 300

######################################################################################
# Layouts
Base = 'Base.html'


######################################################################################

# JavaScript Folder
__JavaScript = 'JavaScript/'


#################
# important functions
__MainScripts = __JavaScript + 'MainScripts/'

JQueryScript = __MainScripts + 'jquery-3.3.1.js'
BootStrapScript = __MainScripts + 'BootStrap.js'
MiniBootStrapScript = __MainScripts + 'MiniBootStrap.js'
DropBoxScript = __MainScripts + 'BodyLoadScript.js'
JQueryRotateScript = __MainScripts + 'JQueryRotate.js'


####################
# Global Functions
__Global_Scripts = __JavaScript + 'GlobalFunctions/'

CheckLenScript = __Global_Scripts + 'CheckLen.js'
CheckinputLenScript = __Global_Scripts + 'CheckinputLen.js'

CheckPasswordScript = __Global_Scripts + 'CheckPassword.js'
CheckPatternScript = __Global_Scripts + 'CheckPattern.js'

TrigerMessageScript = __Global_Scripts + 'TriggerMessage.js'
ErrorFunctionScript = __Global_Scripts + 'SetError_Function.js'

AddPictureScript = __Global_Scripts + 'AddPicture.js'

TrigerFormScript = __Global_Scripts + 'TriggerForm.js'

CheckNameScript = __Global_Scripts + 'CheckName.js'


###################
# Pages Scripts
PagesScripts = __JavaScript + 'PagesScripts/'

######################################################################################
# CSS Folder
__CSS = 'CSS/'

# Main CSS Folders
__MainCSS = __CSS + 'MainCSS/'

AllPagesCSS = __MainCSS + 'AllPagesCSS.CSS'

# Boot Strap
BootStrapCSS = __MainCSS + 'BootStrap/bootstrap.css'
MiniBootStrapCSS = __MainCSS + 'BootStrap/bootstrap.min.css'

###################
# Pages CSS
PagesCSS = __CSS + 'PagesCSS/'


######################################################################################
# BackEnd Pages
__BackEnd = __HOST + '/BackEnd/'

CheckName = __BackEnd + 'CheckName'
CheckEmail = __BackEnd + 'CheckEmail'

LogOut = __BackEnd + 'LogOut'

GetPosts = __BackEnd + 'GetPosts'

MakeCommentPage = __BackEnd + 'MakeComment'
LikeDisLikePostPage = __BackEnd + 'LikeDisLikePost'

DeletePostPage = __BackEnd + 'DeletePost'

GetNotificationsPage = __BackEnd + 'GetNotifications'

######################################################################################
# Small Headers
__Headers = 'Headers/'

##################
__BasicHeaders = __Headers + 'BasicHeaders/'

NavBar = __BasicHeaders + 'NavBar.html'
UserLogged = __BasicHeaders + 'UserLogged.html'
UserNotLogged = __BasicHeaders + 'UserNotLogged.html'
Notifications_Header = __BasicHeaders + 'Notifications_Header.HTML'


Header = __Headers + 'Header.html'


def GetLinks(String):
    Links = []
    while True:
        Start = String.find('[')
        if Start == -1:
            return
        String = String[Start:]

        End = String.find(']')
        if End == -1:
            return
        Text = String[:End+1]
        String = String[End+1:]

        for i in range(len(String)):
            if String[i] != ' ':
                if String[i] != '(':
                    return
                else:
                    String = String[i:]
                    break

        Start = String.find('(')
        if Start == -1:
            return
        String = String[Start:]

        End = String.find(')')
        if End == -1:
            return
        Link = String[:End+1]
        String = String[End+1:]

        Links.append([Text, Link])


Test = 'My Link is ss[Hady]   (http://findhouse.com) . i (Am) [Here]    (Because   ) Of You'
Test2 = '[My Link is (HAHAHA)(]      (   )'
Test3 = ''
GetLinks(Test3)

