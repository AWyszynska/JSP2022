import sys, re
import numpy

def zadanie(x):
    x = str(x)
    x = re.findall('\w+', x)
    #print(x)
    dane = [int(j) for j in x if type(j) == int or j.isdigit()] 
    B = [numpy.mean(dane), numpy.std(dane), numpy.var(dane)]
    return B

if len(sys.argv) == 1:
    a = sys.stdin.read()
else:
    a = sys.argv[1:]
B = zadanie(a)
print("Wartość Średnia: ", B[0])
print("Wariancja: ", B[2])
print("Odchylenie standardowe: ", B[1])
