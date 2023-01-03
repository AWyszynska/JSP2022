import random
import time

wartoscidla100 = []
wartoscidla200 = []
wartoscidla300 = []
t1 = time.time()

def sortowanie_babelkowe(x):
    for i in range(0, len(x) - 1):
        for j in range(0, len(x) - 1):
            if x[j + 1] < x[j]:
                x[j + 1], x[j] = x[j], x[j + 1]
    return x

for i in range(0, 100):
        i = random.randint(0, 20)
        wartoscidla100.append(i)
print(sortowanie_babelkowe(wartoscidla100))
t2 = time.time()
print("Czas:  ",t2-t1)

for i in range(0, 200):
        i = random.randint(0, 20)
        wartoscidla200.append(i)
print(sortowanie_babelkowe(wartoscidla200))
t2 = time.time()
print("Czas:  ",t2-t1)

for i in range(0, 300):
        i = random.randint(0, 20)
        wartoscidla300.append(i)
print(sortowanie_babelkowe(wartoscidla300))
t2 = time.time()
print("Czas:  ",t2-t1)
