class Quadrato:
	
	def __init__(self, lato):
		self.lato = lato
	def __repr__(self):
		return "Quadrato(", self.lato, ")"
	def perimetro(self):
		print self.lato*4
	def area(self):
		print self.lato*self.lato
		
q = Quadrato(5)
print q.lato
print q.perimetro()
print q.area()
