import math
a = int(input("podaj wartość przy x^2: "))
b = int(input("podaj wartośc przy x: "))
c = int(input("Podaje wyraz wolny: "))
d = b**2-4*a*c
print(d)
if a==0:
    print("to nie jest funkcja kwadratowa")

elif d>0:
    e = (-b-math.sqrt(d))/(2*a)
    f = (-b+math.sqrt(d))/(2*a)
    print(e)
    print(f)

elif d==0:
    g = -b/2*a
    print (g)

elif d<0:
    print("nie ma miejsc zerowych")