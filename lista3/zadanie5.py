import re
a = input("Podaj Hasło: ")
znaki = len(a)<6
if (znaki):
        print("Haslo powinno miec przynajmniej 6 znaków")
znakii = len(a)>11
if (znakii):
        print("Haslo nie moze wiecej niz 10 znakow")
liczby = "[0-9]"
liczby1 = re.findall(liczby, a)
if (not liczby1):
        print("Hasło powinno mieć przynajmniej jedną cyfre")
duze_litery = "[A-Z]"
duze_litery1 = re.findall(duze_litery, a)
if (not duze_litery1):
        print("Haslo powinno miec przynajmniej jedna duza litere")
male_litery = "[a-z]"
male_litery1 = re.findall(male_litery, a)
if (not male_litery1):
        print("Haslo powinno miec przynajmniej jedna mala litere")
znak_specjalny = "[$#@]"
znak_specjalny1 = re.findall(znak_specjalny, a)
if (not znak_specjalny1):
        print("Wpisz przynajmniej jeden znak specjalny")
if((not znaki) and liczby1 and duze_litery1 and male_litery1 and znak_specjalny1 and (not znakii)):
        print("\nPoprawne Haslo")
else:
        print("\nNiepoprawne Haslo")
