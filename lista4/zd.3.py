a = int(input())
import math
def sin_radiany_na_stopnie(x):
    return math.sin(math.radians(x))
def sin_stopnie_na_radiany(x):
    return math.sin(math.degrees(x))
def cos_radiany_na_stopnie(x):
    return math.cos(math.radians(x))
def cos_stopnie_na_radiany(x):
    return math.cos(math.degrees(x))
print("Sinus - stopnie na radiany: ",sin_stopnie_na_radiany(a))
print("Sinus - radiany na stopnie: ",sin_radiany_na_stopnie(a))
print("Cosinus - stopnie na radiany: ",cos_stopnie_na_radiany(a))
print("Cosinus - radiany na stopnie: ",cos_radiany_na_stopnie(a))   