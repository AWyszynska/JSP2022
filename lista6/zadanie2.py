stala = 3
def Szyfr_Cezara(x):
    litery = ""
    for i in range(len(x)):
        if ord(x[i])>122-stala:
            litery += chr(ord(x[i]) + stala - 26 )
        else:
            litery += chr(ord(x[i]) + stala)
    return litery
a = input()
print(Szyfr_Cezara(a))
    