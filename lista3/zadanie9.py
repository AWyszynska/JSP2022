m = int(input("Liczba wiersz: "))
n = int(input("Liczba kolumn: "))
def b():
    for i in range(1,m+1):
        for j in range(1,n+1):
            print('{:^5}' .format(i*j)," ",end = ' ')
        print()
b()
        
