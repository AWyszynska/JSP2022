#import zadanie3
otworz = 'pesele.txt'
plik = open(otworz,'r')
lines = plik.readlines()
cc = [i[0:11] for i in lines]
poprawne = []
def sprawdz_pesel(x):
    tablica = []
    for i in range(0,15):
        wyniki = int(x[i][0])*1 + int(x[i][1])*3 + int(x[i][2])*7 + int(x[i][3])*9 + int(x[i][4])*1 + int(x[i][5])*3 + int(x[i][6])*7 + int(x[i][7])*9 + int(x[i][8])*1 + int(x[i][9])*3
        tablica.append(str(wyniki))
    return tablica

pliki = 'zadanie44.txt'
zapisz = open(pliki,"w")

wartości = sprawdz_pesel(cc) 
ostatniezwartosci = [] 
for lines in wartości:
    ostatniezwartosci.append(10 - int(lines[-1]))
dd = [str(i) for i in ostatniezwartosci]
hh = []

for i in range(0,15):
    if cc[i][10] == dd[i]:
        hh.append(cc[i])

for i in range(0,15):
    if int(hh[i][9])%2 == 0:
        x  = " kobieta "
    if int(hh[i][9])%2 == 1:
        x  = " mężczyzna  "
    A = hh[i][0:2]
    C = hh[2][4:6]
    if int(hh[i][2])%2 == 0:
        B = ('0'+hh[i][3])
    if int(hh[i][2])%2 == 1:
        B = ('1'+hh[i][3])
    print('Pesel: ','\n', C,'-',B,'-',A,' ','Płeć: ',x,'\n')
    koniec = ('Pesel: ','\n', C,'-',B,'-',A,' ','Płeć: ',x)
    koniec2 = str(koniec)
    zapisz.write( koniec2)
zapisz.close()


























