class Persona:
	def cambiaNome(self, nome):
		self.nome = nome
	def cambiaCognome(self, cognome):
		self.cognome = cognome
	def cambiaCitta(self, nuovaCitta):
		self.citta = nuovaCitta

mario = Persona()
mario.nome = "Mario"
mario.cognome = "Rossi"
mario.citta = "Roma"
mario.eta = 57
mario.cambiaCitta("Milano")

print mario.nome
print mario.citta
