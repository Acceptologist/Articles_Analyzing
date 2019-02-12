from django import template
from Python import init

register = template.Library()


@register.filter(name='GetLink')
def GetLink(Result):
    return init.Article + str(Result['id'])


@register.filter(name='GetButtonValue')
def GetButtonValue(Result):
    return Result['GetButtonValue']


@register.filter(name='GetResult')
def GetResult(Result):
    if Result['GetResult'] == 'Done':
        return 'TriggerMessage(3000, "#53A01A", "<p>Posted</p>");'
    return 'TriggerMessage(3000, "#53A01A", "<p>Edited</p>");'


@register.filter(name='GetPage')
def GetPage(Result):
    if Result['GetResult'] == 'Done':
        return init.MakeArticle
    return init.EditArticle + str(Result['id'])
