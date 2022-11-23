a = int(input())
def sum(b):
    d = 1
    c= 0
    for d in range(1, b+1):
        c = c + 1/d
    return c

print(sum(a))