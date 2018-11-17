from django.shortcuts import render
from Python import init
from django.http import HttpResponse


def SignUP(request):
    return Response()


def Response()
    if request.method == 'POST' and 'N' in request.POST and (
            'E' in request.POST and 'P' in request.POST and (
            request.META.get('HTTP_REFERER') is not None)):
        
        from Python import URL
        return HttpResponse(request.META.get('HTTP_REFERER'))

    return render(request, 'Register/SignUP.html', {
        'init': init,
        'title': 'Sign UP',
        'request': request.META.get('HTTP_REFERER')
    })


def login(request):
    return render(request, 'Register/Login.html', {
        'init': init,
        'title': 'Log in'
    })
