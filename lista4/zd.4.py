print("Podaj numer elementu ciagu ktory chcesz obliczyc: ")
n = int(input())
print("Podaj wartosc pierwszego elementu ciagu: ")
a = int(input())
print("Podaj wartosc iloczynu ciagu: ")
q = int(input())
def ciag(n,a,q):
    return a*q**(n-1)
print(n,"Wyraz ciagu ma wartosc",ciag(n,a,q))