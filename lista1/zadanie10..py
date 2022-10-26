import cmath
import math

z = complex(2,6)
print(z)
a = cmath.sin(z)
b = cmath.cos(z)
print("wartość rzeczywista sin:",a.real)
print("wartość urojona sin:",a.imag)
print("wartość rzeczywista cos:",b.real)
print("wartość urojona cos:", b.imag)
print(a**2+b**2==1)
