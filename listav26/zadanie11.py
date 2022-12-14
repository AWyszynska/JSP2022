import zadanie12

a = int(input("Bok a: "))
b = int(input("Bok b: "))
c = int(input("Bok c: "))

if a+b > c and a+c > b and b+c > a:
    print(zadanie12.obwod(a, b, c))
    print(zadanie12.pole(a, b, c))
    print(zadanie12.rodzaj1(a, b, c))
    print(zadanie12.rodzaj2(a, b, c))
