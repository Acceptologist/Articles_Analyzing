from Python.GlobalFunctions import Returns


def Hash_Users(User):
    return 'MY' + User


def Hash_Articles(Article):
    return 'MYNA' + Article


def Hash_Comments(Comment):
    return 'MYNAME' + Comment


def Hash_LikeDisLike(LikeDisLike):
    return 'MYNAMEHA' + LikeDisLike


def Hash_Notifications(Notification):
    return 'MYNAMEHADY' + Notification


###############################################################################
def Get_Hashed_Users(User):
    if len(User) < 2:
        return Returns(-1, '', 'Getting User From Hashing')
    return Returns(1, User[2:])


def Get_Hashed_Articles(Article):
    if len(Article) < 4:
        return Returns(-1, '', 'Getting Article From Hashing')
    return Returns(1, Article[4:])


def Get_Hashed_Comments(Comment):
    if len(Comment) < 6:
        return Returns(-1, '', 'Getting Comment From Hashing')
    return Returns(1, Comment[6:])


def Get_Hashed_LikeDisLike(LikeDisLike):
    if len(LikeDisLike) < 8:
        return Returns(-1, '', 'Getting LikeDisLike From Hashing')
    return Returns(1, LikeDisLike[8:])


def Get_Hashed_Notifications(Notification):
    if len(Notification) < 10:
        return Returns(-1, '', 'Getting Notification From Hashing')
    return Returns(1, Notification[10:])


###############################################################################
def GetAllFromHashing(AllData):
    Hashed_Data = Returns(1)
    Hashed_Data['Data'] = {}
    for Data in AllData:
        if Data['Type'] == 'Users':
            Result = Get_Hashed_Users(Data['Data'])
        elif Data['Type'] == 'Articles':
            Result = Get_Hashed_Articles(Data['Data'])
        elif Data['Type'] == 'Comments':
            Result = Get_Hashed_Comments(Data['Data'])
        elif Data['Type'] == 'LikeDisLike':
            Result = Get_Hashed_LikeDisLike(Data['Data'])
        elif Data['Type'] == 'Notifications':
            Result = Get_Hashed_Notifications(Data['Data'])
        elif Data['Type'] == 'Date':
            Result = Returns(1, str(Data['Data']))
        else:
            Result = Returns(1, Data['Data'])

        if Result['Result'] == -1:
            return Returns(-1, 'Getting '+Data['Key']+' From Hashing', Result['Error'])
        else:
            Hashed_Data['Data'][Data['Key']] = Result['Data']

    return Hashed_Data
