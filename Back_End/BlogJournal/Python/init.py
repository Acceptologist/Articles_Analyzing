# WebSite Name
WebSiteName = 'Blog Journal'


######################################################################################
# Picture Folder
__Pictures = 'Pictures/'

# Main Pictures
LOGO = __Pictures + 'LOGO.PNG'
ProfilePicture = __Pictures + 'ProfilePicture.JPG'
OfflineUsers = __Pictures + 'OfflineUsers.PNG'


######################################################################################
# Pages Status
PagesStatus = 'PagesStatus/'

UnAuthurithedUserPage = PagesStatus + 'UnAuthurithedUserPage.html'
LogOutPage = PagesStatus + 'LogOutPage.html'


######################################################################################
# Pages
__HOST = 'http://127.0.0.1:8000'

SignUP = __HOST + '/Register/SignUP'
Login = __HOST + '/Register/Login'

Main = __HOST
MakeBlog = __HOST + '/Blogs/Make_Blog'


######################################################################################
# Messages
MessageBox = 'MessageBoxs/MessageBox.html'


######################################################################################
# Length

# Sign UP
Name_Len = 40      # 100
Email_Len = 100     # 150
Password_Len = 40      # 100
Blog_Len = 2000     # 2100


######################################################################################
# Layouts
Base = 'Base.html'


######################################################################################

# JavaScript Folder
__JavaScript = 'JavaScript/'


#################
# important functions
JQueryScript = __JavaScript + 'jquery-3.3.1.js'
DropBoxScript = __JavaScript + 'DropBox.js'


####################
# Global Functions
__Global_Scripts = __JavaScript + 'GlobalFunctions/'

CheckinputLenScript = __Global_Scripts + 'CheckinputLen.js'
CheckLenScript = __Global_Scripts + 'CheckLen.js'
ConfirmPasswordScript = __Global_Scripts + 'ConfirmPassword.js'
CheckPatternScript = __Global_Scripts + 'CheckPattern.js'

TrigerMessageScript = __Global_Scripts + 'TrigerMessage.js'
ErrorFunctionScript = __Global_Scripts + 'ErrorFunction.js'


###################
# Pages Scripts
SignUPScript = __JavaScript + 'Register/SignUPScript.js'
LoginScript = __JavaScript + 'Register/LoginScript.js'

MainScript = __JavaScript + 'Blogs/MainScript.js'
MakeBlogScript = __JavaScript + 'Blogs/MakeBlogScript.js'


######################################################################################
# CSS Folder
__CSS = 'CSS/'

# Main CSS Folders
HeaderCSS = __CSS + 'Header.CSS'
CenterCSS = __CSS + 'Center.CSS'
FooterCSS = __CSS + 'Footer.CSS'


######################################################################################
# BackEnd Pages
__BackEnd = __HOST + '/BackEnd/'

BackEnd_ChekcUser = __BackEnd + 'CheckUser'
BackEnd_LogOut = __BackEnd + 'LogOut'


######################################################################################
# Small Headers
__Headers = 'Headers/'
__BasicHeaders = __Headers + 'BasicHeaders/'

NavBar = __BasicHeaders + 'NavBar.html'
UserLogged = __BasicHeaders + 'UserLogged.html'
UserNotLogged = __BasicHeaders + 'UserNotLogged.html'


######################################################################################
# Big Headers
AllHeaders = __Headers + 'AllHeaders.html'
LoggedHeaders = __Headers + 'LoggedHeaders.html'
NotLoggedHeaders = __Headers + 'NotLoggedHeaders.html'


######################################################################################
# Errors

Errors = [
    {'API': 1, 'Type': 'Ajax', 'Message': 'Failed To Make Ajax Call To The Page'},
    {'API': 2, 'Type': 'JSON', 'Message': 'Failed To Convert To JSON'}
]


print(Errors[0]["Message"])
