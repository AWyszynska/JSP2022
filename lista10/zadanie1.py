import math
class Kolo():
    def __init__(self,r):
        self.r = r
    def pole(self):
        print("Pole:  ",2*math.pi*self.r**2)
    def obwod(self):
        print("Obwod: ",2*math.pi*self.r)




kolo = Kolo(4)
kolo.obwod()
