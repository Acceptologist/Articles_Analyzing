def Delete_Session(Request):
    try:
        del Request.session["ID"]
        del Request.session["Name"]
        del Request.session["Email"]
        del Request.session["Date"]
        del Request.session["Picture"]
        del Request.session["Articles_Number"]
        Request.session.modified = True
        return Returns(1)
    except Exception as e:
        return Returns(-1)


def Returns(Result='', Data='', Error=''):
    return {
        'Result': Result,
        'Data': Data,
        'Error': Error
    }


def SESSION(Request):
    if 'Name' in Request.session:
        return True
    return False
