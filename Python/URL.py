def GetURL(Request):
    return Request.META["HTTP_ORIGIN"] + Request.META["PATH_INFO"]


def GetREFERER(Request):
    if Request.META["HTTP_REFERER"] is None:
        return ''.split()
    return Request.META["HTTP_REFERER"].split('?')[0]


def REFERER_is_Set(Request):
    if Request.META["HTTP_REFERER"] is None:
        return False
    return True
