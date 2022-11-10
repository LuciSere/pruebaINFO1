#clases caso 1 y 2
class Vehiculo:
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas
		self.name = "VEHICULO"

	def getColor(self):
		return self.color

	def setColor(self, nuevo_color):
		self.color = nuevo_color

	def getRuedas(self):
		return self.ruedas

	def setRuedas(self, nuevo_ruedas):
		self.ruedas = nuevo_ruedas

	def __str__(self):
		return f"{self.name} Color: {self.color}. Ruedas: {self.ruedas}."

class Coche(Vehiculo):
	def __init__(self, color, ruedas, velocidad, cilindrada):
		super().__init__(color, ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada
		self.name = "COCHE"

	def getVelocidad(self):
		return str(self.velocidad) + ' km/h '

	def setVelocidad(self, nuevo):
		self.velocidad = nuevo

	def getCilindrada(self):
		return str(self.cilindrada) + ' cc '

	def setCilindrada(self, nuevo):
		self.cilindrada = nuevo	

	def __str__(self):
		return super().__str__() + f' Velocidad: {self.getVelocidad()}. Cilindrada: {self.getCilindrada()}.'

class Bicicleta(Vehiculo):
	def __init__(self, color, ruedas, tipo):
		super().__init__(color, ruedas)
		self.tipo = tipo # urbana o deportiva
		self.name = "BICICLETA"

	def getTipo(self):
		return self.tipo

	def setTipo(self, nuevo):
		self.tipo = nuevo	

	def __str__(self):
		return super().__str__() + f' Tipo: {self.tipo}.'

class Motocicleta(Bicicleta):
	def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
		super().__init__(color, ruedas, tipo)
		self.velocidad = velocidad
		self.cilindrada = cilindrada
		self.name = "MOTOCICLETA"

	def getVelocidad(self):
		return str(self.velocidad) + ' km/h '

	def setVelocidad(self, nuevo):
		self.velocidad = nuevo

	def getCilindrada(self):
		return str(self.cilindrada) + ' cc '

	def setCilindrada(self, nuevo):
		self.cilindrada = nuevo	

	def __str__(self):
		return  super().__str__() + f' Velocidad: {self.getVelocidad()}. Cilindrada: {self.getCilindrada()}.'

class Camioneta(Coche):
	def __init__(self, color, ruedas, velocidad, cilindrada, carga):
		super().__init__(color, ruedas, velocidad, cilindrada)
		self.carga = carga #en kg
		self.name = "CAMIONETA"

	def getCarga(self):
		return str(self.carga) + ' kg'

	def setCarga(self, nuevo):
		self.carga = nuevo	

	def __str__(self):
		return super().__str__() + f' Carga: {self.getCarga()}.'