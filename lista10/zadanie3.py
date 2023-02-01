from itertools import combinations
class tablica():
    l = []
    def __init__(self, l):
        self.l = l

    def tablica(self):
        k = list(combinations(self.l, 3))
        w = []
        for i in k:
            if sum(i) == 0:
                w.append(list(i))
        return w

tt = tablica([1, 2,-3,4,5,-9])
print(tt.tablica())
