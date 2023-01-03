import random
import time

t1 = time.time()
zastowaniedla100 = []
zastowaniedla200 = []
zastowaniedla300 = []


def Sortowanie_przez_wstawianie(z):      # 1, 3, 6, 4, 2, 4, 0, 5
    for j in range(1, len(z)):
        i = j - 1
        while i >= 0:
            if z[i + 1] < z[i]:
                z[i + 1], z[i] = z[i], z[i + 1]
            i -= 1
    return z

for i in range(0, 100):
        i = random.randint(0, 20)
        zastowaniedla100.append(i)
print(Sortowanie_przez_wstawianie(zastowaniedla100))
t2 = time.time()
print("Czas:  ",t2-t1)


for i in range(0, 200):
        i = random.randint(0, 20)
        zastowaniedla200.append(i)
t2 = time.time()
print(Sortowanie_przez_wstawianie(zastowaniedla200))
print("Czas:  ",t2-t1)


for i in range(0, 300):
        i = random.randint(0, 20)
        zastowaniedla300.append(i)
t2 = time.time()
print(Sortowanie_przez_wstawianie(zastowaniedla300))
print("Czas:  ",t2-t1)
