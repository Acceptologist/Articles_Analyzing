def Hash_Users(String):
    return 'MY' + String


def Get_Hashed_Users(String):
    if len(String) < 3:
        return [-1, '']
    return [1, String[2:]]


def Hash_Posts(String):
    return 'MYNA' + String


def Get_Hashed_Posts(String):
    if len(String) < 5:
        return [-1, '']
    return [1, String[4:]]
