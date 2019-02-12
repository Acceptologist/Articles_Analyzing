def __Class(Class):
    return ' class="' + Class + '" ' if Class != '' else ' '


def __ID(ID):
    return ' id="' + ID + '" ' if ID != '' else ' '


def __URL(URL):
    return ' href="' + str(URL) + '" ' if URL != '' else ' '


def __Click(Click):
    return ' onclick="' + Click + '" ' if Click != '' else ' '


def __Value(Value):
    return ' value="' + Value + '" ' if Value != '' else ' '


def __Type(Type=''):
    return ' type="' + Type + '" ' if Type != '' else ' type="text" '


def Div(Text, Class='', ID=''):
    return '<div ' + __ID(ID) + __Class(Class) + '>' + Text + '</div>'


def P(Text, Class='', ID=''):
    return '<p ' + __ID(ID) + __Class(Class) + '>' + Text + '</p>'


def Span(Text, Class=''):
    return '<span ' + __Class(Class) + '>' + Text + '</span>'


def Strong(Text, Class=''):
    return '<strong ' + __Class(Class) + '>' + Text + '</strong>'


def A(URL, Text, Class='', Click=''):
    return '<a ' + __URL(URL) + __Class(Class) + __Click(Click) + '>' + Text + '</a>'


def AButton(Text, Class='', Click=''):
    return '<a ' + __Class(Class) + __Click(Click) + '>' + Text + '</a>'


def InputImage(SRC, ID='', Click=''):
    return '<input type="image" src="/Static/' + SRC + '" ' + __ID(ID) + __Click(Click) + '">'


def Input(Type, Value='', ID='', Class='', Click=''):
    return '<input ' + __Type(Type) + __Value(Value) + __ID(ID) + __Class(Class) +\
           __Click(Click) + '>'
