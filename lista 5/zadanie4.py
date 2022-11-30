klucz = {'a':'y',
         'e':'i',
         'i':'o',
         'o':'a',
         'y':'e'}

def crypt(x):
    crypted = ""
    for j in x:
        if j in klucz.keys():
            crypted += klucz[j]
        else:
            crypted += j
    return crypted

a = input()
print(crypt(a))

def decrypt(x):
    decrypted = ""
    for j in x:
        foundKey = ""
        for key, item in klucz.items():
            if(j == item):
                foundKey = key
        if foundKey != "":
            decrypted += foundKey
        else:
            decrypted += j
    return decrypted
print(decrypt(a))