a = float(input())
import math
def sin_radiany_na_stopnie(x):
    return (x*180)/math.pi
def sin_stopnie_na_radiany(x):
    return (x*math.pi)/180


print("Sinus - stopnie na radiany: ",sin_stopnie_na_radiany(a))
print("Sinus - radiany na stopnie: ",sin_radiany_na_stopnie(a))
   