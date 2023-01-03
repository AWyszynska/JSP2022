import time

n = int(input("Który wyraz ciągu chcesz obliczyć?:  "))
def Fibonacci_rekurencja(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return Fibonacci_rekurencja(n - 1) + Fibonacci_rekurencja(n - 2)

def Fibonacci_iteracja(n):
    a = 0
    b = 1
    for i in range(0, n):   
        a, b = b, a + b     
    return a

time_0 = time.time()
for i in range(0, n):
    print(Fibonacci_rekurencja(i))
print(time.time() - time_0)

time_0 = time.time()
for i in range(0, n):
    print(Fibonacci_iteracja(i))
print(time.time() - time_0)
