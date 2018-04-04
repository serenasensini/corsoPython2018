class Quadrato:
    
    lato = 0
    
    def __init__(self, nuovoLato):
        self.lato = nuovoLato
    def __repr__(self):
        return "Quadrato(" + str(self.lato) + ")"
    def perimetro(self):
        return self.lato*4
    def area(self):
        return self.lato*self.lato
       
q = Quadrato(5)
print q.perimetro()
print q.area()
print q.__repr__()