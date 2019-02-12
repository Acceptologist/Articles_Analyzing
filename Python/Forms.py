from django import forms
from Python import init


class Forms:
    __isValid = False

    def CheckKey(self, Keys):
        for i in range(len(Keys)):
            if Keys[i] not in self.cleaned_data:
                return False
        return True

    def is_Valid(self, Keys):
        # Must Write is_valid function first so Cleaned_Data is defined
        if self.is_valid() and self.CheckKey(Keys):
            self.__isValid = True
            return True
        return False

    def Get(self, Key):
        if self.__isValid:
            return self.cleaned_data[Key]
        return ''


############################################################################################
# Back End Forms
# Check Name Form
class CheckNameForm(forms.Form, Forms):
    Name = forms.CharField(max_length=init.Name_Len, min_length=1)

    def isValid(self):
        return self.is_Valid(["Name"])

    def GetName(self):
        return self.Get('Name')


# Check Email Form
class CheckEmailForm(forms.Form, Forms):
    Email = forms.CharField(max_length=init.Email_Len, min_length=1)

    def isValid(self):
        return self.is_Valid(["Email"])

    def GetEmail(self):
        return self.Get('Email')


# Check Number
class CheckPostsNumberForm(forms.Form, Forms):
    Number = forms.IntegerField(max_value=1000000, min_value=0)

    def isValid(self):
        return self.is_Valid(['Number'])

    def GetNumber(self):
        return self.Get('Number')


# Check Number
class MakeCommentForm(forms.Form, Forms):
    ID = forms.IntegerField(max_value=1000000, min_value=0)
    Comment = forms.CharField(max_length=init.Comment_Len, min_length=1)

    def isValid(self):
        return self.is_Valid(['ID', 'Comment'])

    def GetID(self):
        return self.Get('ID')

    def GetComment(self):
        return self.Get('Comment')


class LikeDisLikeForm(forms.Form, Forms):
    ID = forms.IntegerField(max_value=1000000, min_value=0)
    Type = forms.IntegerField(max_value=1, min_value=0)

    def isValid(self):
        return self.is_Valid(['ID', 'Type'])

    def GetID(self):
        return self.Get('ID')

    def GetType(self):
        return self.Get('Type')


############################################################################################
# Register Forms
# SignUP Form
class SignUPForm(forms.Form, Forms):
    Name = forms.CharField(max_length=init.Name_Len, min_length=1)
    Email = forms.CharField(max_length=init.Email_Len, min_length=1)
    Password = forms.CharField(max_length=init.Password_Len, widget=forms.PasswordInput,
                               min_length=1)

    def isValid(self):
        return self.is_Valid(["Name", "Email", "Password"])

    def GetName(self):
        return self.Get('Name')

    def GetEmail(self):
        return self.Get('Email')

    def GetPassword(self):
        return self.Get('Password')


# Log in Form
class LoginForm(forms.Form, Forms):
    Email = forms.CharField(max_length=init.Email_Len, min_length=1)
    Password = forms.CharField(max_length=init.Password_Len, widget=forms.PasswordInput,
                               min_length=1)

    def isValid(self):
        return self.is_Valid(["Email", "Password"])

    def GetEmail(self):
        return self.Get('Email')

    def GetPassword(self):
        return self.Get('Password')


############################################################################################
# Articles Forms
# Make Article Form
class MakeArticleForm(forms.Form, Forms):
    Title = forms.CharField(max_length=init.ArticleTitle_Len, min_length=1)
    Tags = forms.CharField(max_length=init.ArticleTags_Len, required=False)
    Article = forms.CharField(max_length=init.Article_Len, min_length=1)

    def isValid(self):
        return self.is_Valid(["Title", "Article", "Tags"])

    def GetTitle(self):
        return self.Get('Title')

    def GetArticle(self):
        return self.Get('Article')

    def GetTags(self):
        return self.Get('Tags')


############################################################################################
# Profile Forms
# Password Form
class PasswordForm(forms.Form, Forms):
    OldPassword = forms.CharField(max_length=init.Password_Len, widget=forms.PasswordInput,
                                  min_length=1)
    Password = forms.CharField(max_length=init.Password_Len, widget=forms.PasswordInput,
                               min_length=1)

    def isValid(self):
        return self.is_Valid(["OldPassword", "Password"])

    def GetOldPassword(self):
        return self.Get('OldPassword')

    def GetPassword(self):
        return self.Get('Password')


# Image Form
class ImageForm(forms.Form, Forms):
    File1 = forms.FileField(max_length=init.Picture_Len)

    def isValid(self):
        return self.is_Valid(['File1'])

    def GetFile(self):
        return self.Get('File1')
