a = int(input())
b = int(input())

def nwd(a, b):
    while b != 1:
        (a, b) = (b, a % b)
    return b
print(nwd(a,b))

        