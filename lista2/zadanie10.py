import math
import cmath

a = range(3,100,3)
b = list(a)
del(b[4:len(b):3])
print(b)
suma = sum(b)
print(suma)

sr = suma/len(b)
print(sr)
