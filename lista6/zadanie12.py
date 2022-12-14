import math

def obwod(a, b, c):
    return print(a + b + c)

def pole(a, b, c): 
    p = 1 / 2 * (a + b + c)
    P1 = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return print(P1)

def rodzaj1(a, b, c):
    if (a == b) and (a == c):
        return print("Trójkąt równoboczny")
    if ((a == b) and (a != c)) or ((a == c) and (a != b)) or ((b == c) and (b != a)):
        return print("Trójkąt równoramienny")
    if (a != b) and (a != c) and (b != c):
        return print("Trójkąt różnoboczny")

def rodzaj2(a, b, c):
    if a == math.sqrt(b ** 2 + c ** 2):
        print("Trójkąt prostokątny")
    elif b == math.sqrt(a ** 2 + c ** 2):
        print("Trójkąt prostokątny")
    elif c == math.sqrt(a ** 2 + b ** 2):
        print("Trójkąt prostokątny")
    x = (c ** 2 + b ** 2 - a ** 2) / (2 * b * c) 
    y = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c) 
    z = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b) 
    if ((x < 1) and (x > 0)) and ((y < 1) and (y > 0)) and ((z< 1) and (z > 0)):
        return print("Trójkąt ostrokątny")
    x = math.degrees(math.acos(x))
    y = math.degrees(math.acos(y))
    z = math.degrees(math.acos(z))
    if (x > 90) or (y > 90) or (z > 90):
        return print("Trójkąt rozwartokątny")
