from django.http import JsonResponse, HttpResponseRedirect
from Python import Hashing, init, GlobalFunctions
from Register.models import Users


def CheckUser(Request):
    try:
        Users.objects.get(Email=Hashing.Hash_Users(Request.POST["E"]))
    except Users.DoesNotExist:
        return JsonResponse({'Result': '0'})
    else:
        return JsonResponse({'Result': '1'})


def LogOut(Request):
    GlobalFunctions.Delete_Session(Request)
    return HttpResponseRedirect(init.Main)
