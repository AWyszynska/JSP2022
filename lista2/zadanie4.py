a = input()
b=a[0]
x = a.replace(b, "$")
d = list(x)
d[0] = b
print("".join(d))