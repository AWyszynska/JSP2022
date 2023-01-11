import random
a = int(input("ile razy:  "))
pesel = []
def wygeneruj_pesel(x):
    for i in range(0,x):
        litera1 = random.randint(0, 9)
        litera2 = random.randint(0, 9)
        litera3 = random.randint(0, 8)
        litera4 = random.randint(0, 9)
        if(litera3%2 == 0 and litera4 == 0):
            litera4 = litera4 + random.randint(0, 9)
        if(litera3%2 == 1):
            litera4 = random.randint(0, 2)
        litera5 = random.randint(0, 3)
        if(litera4 == 2 and litera3%2 == 0):
            litera5 = random.randint(0, 2)
        litera6 = random.randint(0, 9)
        if((litera4 != 4 and litera4 != 6 and litera4 > 9 and litera5 == 3  ) or (litera4%2 == 0 and litera4 > 8 and litera5 == 3)):
            litera6  = random.randint(0, 1)
        if((litera3%2 == 1 and litera4 == 1 and litera5 == 3)):
            litera6  = 0
        if((litera4 == 4 and litera5 == 3) or (litera4 == 6 and litera5 == 3 )or( litera4 == 9 and litera5 == 3)):
            litera6  = 0
        if(litera5 == 0):
            litera6  = random.randint(1, 9)
        if(litera4 == 2 and litera3%2 == 0 and litera2%2 == 0):
            litera6 = random.randint(0, 8)
        litera7 = random.randint(0, 9)
        litera8 = random.randint(0, 9)
        litera9 = random.randint(0, 9)
        litera10 = random.randint(0, 9)
        suma = 1*litera1 + 3*litera2 + 7*litera3 + 9*litera4 + 1*litera5 + 3*litera6 + 7*litera7 + 9*litera8 + 1*litera9 + 3*litera10
        suma2 = str(suma)
        ostatnialitera = 10 - int(suma2[-1])
        litera11 = int(ostatnialitera)
        pesel.append(litera1)
        pesel.append(litera2)
        pesel.append(litera3)
        pesel.append(litera4)
        pesel.append(litera5)
        pesel.append(litera6)
        pesel.append(litera7)
        pesel.append(litera8)
        pesel.append(litera9)
        pesel.append(litera10)
        pesel.append(litera11)
        pesel.append("\n")
        all_strings = list(map(str, pesel))
        wynik2 = ''.join(all_strings)
    return(wynik2)

x = wygeneruj_pesel(a)
print(x)
wyg  = str(x)
plik = 'pesel.txt.txt'
zapisz = open(plik,"w")
zapisz.write(wyg)
zapisz.close()














