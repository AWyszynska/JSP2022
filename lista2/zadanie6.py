lista = ["Kasia","Basia","Marek", "Darek"]
lista.append("Józek")
lista.extend("Basia")
lista.extend("Asia")
print(lista)
print(lista[4])
print(lista[0:2])
print(lista[10:14], lista[5:10])
#lista.sorted()
lista.remove("Basia")
print(lista)
len(lista)