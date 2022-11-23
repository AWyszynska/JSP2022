g = int(input())
h = int(input())
j = int(input())
def zmiana(a, b, c):
    a, b, c = a / 255.0, b / 255.0, c / 255.0
 
    cmax = max(a, b, c)    
    cmin = min(a, b, c)    
    diff = cmax-cmin       
 
    if cmax == cmin:
        d = 0

    elif cmax == a:
        d = (60 * ((b - c) / diff) + 360) % 360

    elif cmax == b:
        d = (60 * ((c - a) / diff) + 120) % 360
 
    elif cmax == c:
        d = (60 * ((a - b) / diff) + 240) % 360
 
    if cmax == 0:
        e = 0
    else:
        e = (diff / cmax) * 100

    f = cmax * 100
    return d, e, f

print(zmiana(g, h, j))