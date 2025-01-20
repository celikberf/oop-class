class Circle: 
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap
    
    def alanHesapla(self):
        return self.pi * (self.yaricap ** 2)
    
c1 = Circle()
c2 = Circle(5)

print(f"c1: alan {c1.alanHesapla()} çevre: {c1.cevreHesapla()}")
print(f"c2: alan {c2.alanHesapla()} çevre: {c2.cevreHesapla()}")