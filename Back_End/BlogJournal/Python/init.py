##################################
# Python Folders
# Functions
PY = 'Python/'

# Class

# Pages Functions


###################################
# Layouts

# Layouts
Base = 'Base.html'

# Small Headers
Headers = 'Headers/'
BasicHeaders = Headers + 'BasicHeaders/'

NavBar = BasicHeaders + 'NavBar.html'
UserHeader = BasicHeaders + 'UserHeader.html'
UserNotLoggedHeader = BasicHeaders + 'UserNotLoggedHeader.html'

# Big Headers
AllHeaders = Headers + 'AllHeaders.html'
LoggedHeaders = Headers + 'LoggedHeaders.html'
NotLoggedHeaders = Headers + 'NotLoggedHeaders.html'

# Message
MessageBox = 'MessageBoxs/MessageBox.html'
TrigerErrorMessage = 'MessageBoxs/TriggerErrorMessage.js'

# Pages
SignUP = '/register/signup'
Login = '/register/login'


###################################
# CSS Folder
CSS = 'CSS/'

# Main CSS Folders
HeaderCSS = CSS + 'Header.CSS'
CenterCSS = CSS + 'Center.CSS'
FooterCSS = CSS + 'Footer.CSS'


###################################
# Picture Folder
Pictures = 'Pictures/'

# Main Pictures
LOGO = Pictures + 'LOGO.PNG'
ProfilePicture = Pictures + 'ProfilePicture.JPG'
OfflineUsers = Pictures + 'OfflineUsers.PNG'


###################################
# JavaScript Folder
JavaScript = 'JavaScript/'

# important functions
JQueryScript = JavaScript + 'jquery-3.3.1.js'
DropBoxScript = JavaScript + 'DropBox.js'

# Global Functions
Global_Scripts = JavaScript + 'GlobalFunctions/'

CheckinputLenScript = Global_Scripts + 'CheckinputLen.js'
CheckLenScript = Global_Scripts + 'CheckLen.js'
ConfirmPasswordScript = Global_Scripts + 'ConfirmPassword.js'
CheckPatternScript = Global_Scripts + 'CheckPattern.js'

# Pages Scripts
SignUPScript = 'JavaScript/Register/SignUPScript.js'


###################################
# Length

# Sign UP
Name_Len = 40      # 100
Email_Len = 100     # 150
Password_Len = 40      # 100


def empty(value):
    if not value:
        return True
    else:
        return False


x = None
# print(empty(x))
