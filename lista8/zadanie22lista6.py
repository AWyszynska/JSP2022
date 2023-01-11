def Szyfr_Cezara2(x,y):
    litery = ""
    for i in range(len(x)):
        if ord(x[i])>122-y:
            litery += chr(ord(x[i]) - y - 26 )
        else:
            litery += chr(ord(x[i]) - y)
    return litery
