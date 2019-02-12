from Python import init
from Python.Render import __Render


def UnAuthurithedUserPage(Request, Title):
    return __Render(Request, init.UnAuthurithedUserPage, Title)


def ErrorPage(Request, Title):
    return __Render(Request, init.ErrorPage, Title)


def LogOutPage(Request, Title):
    return __Render(Request, init.LogOutPage, Title)


def NotFoundPage(Request, Title):
    return __Render(Request, init.NotFoundPage, Title)
