class Gustina:
    def __init__(self, povrsinaZemlje, brojStanovnika):
        self.povrsinaZemlje=povrsinaZemlje
        self.brojStanovnika=brojStanovnika

    def IzracunajGustinu(self):
        return self.povrsinaZemlje/self.brojStanovnika
    
z1 = Gustina(10000, 5000)
z2 = Gustina(20000, 5500)
z3 = Gustina(9000, 2000)


print("gustina prve zemlje je : ", z1.IzracunajGustinu())
print("gustina druge zemlje je : ", z2.IzracunajGustinu())
print("gustina trece zemlje je : ", z3.IzracunajGustinu())
