from django.shortcuts import render
from Python import init


def UnAuthurithedUserPage(Request, Title):
    return Render(Request, init.UnAuthurithedUserPage, Title)


def LogOutPage(Request, Title):
    return Render(Request, init.LogOutPage, Title)


def Render(Request, Page, Title):
    return render(Request, Page, {
        'init': init,
        'Title': Title,
        'Session_Name': Request.session["Name"]
    })
