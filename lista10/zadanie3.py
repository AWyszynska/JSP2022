from itertools import combinations
class tablica():
    lista = []
    def __init__(self, l):
        self.l = l

    def trzymEl(self):
        k = list(combinations(self.l, 3))
        w = []
        for i in k:
            if sum(i) == 0:
                w.append(list(i))
        return w

tt = tablica([1, -3, 4, 1, 2, 0, 7, 2, 5, -2, -4, -1])
print(tt.tablica())
