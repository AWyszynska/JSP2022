
class podlisty():
    def __init__(self,lista):
        self.lista = lista
    def wynik(self):
        lists = [[]]
        for i in range(len(self.lista) + 1):
            for j in range(i):
                lists.append(self.lista[j: i])
        print(lists)

lll = [1, 2, 3, 4, 5, 6]
a = podlisty(lll)        
a.wynik()
