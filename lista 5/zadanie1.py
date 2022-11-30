slownik = {
    'zero' : 0,
    'jeden' : 1,
    'dwa' : 2,
    'trzy' : 3,
    'cztery': 4,
    'piec': 5,
    'szesc' : 6,
    'siedem' : 7,
    'osiem' : 8,
    'dziewiec' : 9,
    'dziesiec' : 10,
    }
a = input()
l = len(a)

def funk(d):
    if l <= 8:
        for i in slownik.items():
            if d in slownik.keys():
                return(slownik[d])
    if a[-6:] == ("nascie"):
        for j in slownik.items():
            for key in slownik.keys():
                if d[:3] in key in slownik.keys():
                    x = slownik['jeden']
                    y = slownik[key]
                    return (str(x)+str(y))
                    return(result)
    if a[-8:-3] ==("dzies") or a[-7:-3]==("dzie"):
        for j in slownik.items():
            for key in slownik.keys():
                if d[:3] in key in slownik.keys():
                    z = slownik[key]
                    v = slownik['zero']
                    return(str(z)+str(v))
    if l>=14:
        for j in slownik.items():
            for key in slownik.keys():
                for k in slownik.keys():
                    if d[-4:-1] in key and d[:3] in k in slownik.keys():
                        i = slownik[k]
                        t = slownik[key]
                        return[str(i)+str(t)]

print(funk(a))