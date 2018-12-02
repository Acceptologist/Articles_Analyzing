def GetURL(Request):
    return Request.META["HTTP_ORIGIN"] + Request.META["PATH_INFO"]

