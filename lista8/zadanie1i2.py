import datetime 
import zadanie2lista6
import zadanie22lista6
plik = 'plik_do_szyfrowania.txt.txt'
openplik = open(plik,"r").read()

a = int(input("Podaj liczbe od 1-10: "))

date_today  = datetime.date.today()
month = date_today.month
year = date_today.year
day = date_today.day

g = ['plik_zaszyfrowany','_',a,year,'-',month,'-',day,'.txt']
all_strings = list(map(str, g))
result = ''.join(all_strings)

s = ['plik_deszyfrowany','_',a,year,'-',month,'-',day,'.txt']
all_strings = list(map(str, s))
wynik2 = ''.join(all_strings)

zaszyfrowane = zadanie2lista6.Szyfr_Cezara(openplik,a)

print(zaszyfrowane)

with open(result,'w', encoding="utf-8") as file:
    file.write(zaszyfrowane)

#ZADANIE2

szyfr2 = open(result,'r')
deszyfrowanie = zadanie22lista6.Szyfr_Cezara2(zaszyfrowane,a)
print(deszyfrowanie)
with open(wynik2,'w', encoding="utf-8") as file:
    file.write(deszyfrowanie)












