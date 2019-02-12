from Python.Render import __Render
from Python import init


def Help(Request):
    return __Render(Request, init.Help_Template, 'Help Center')


def Policy(Request):
    return __Render(Request, init.Policy_Template, 'Privacy Policy')
