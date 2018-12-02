def Check_Len(String, Len):
    if len(String) == 0:
        return 'Empty'
    elif len(String) > Len:
        return 'Too Long'
    return 'OK'


def Delete_Session(Request):
    del Request.session["Name"]
    del Request.session["Email"]
    del Request.session["Date"]
    del Request.session["Picture"]
    del Request.session["Blogs_Number"]
    Request.session.modified = True
