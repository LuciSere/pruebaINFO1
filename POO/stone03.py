'''
https://sites.google.com/view/informatorio-poo/level-stone?authuser=0

caso 3
Desarrollar un programa que cargue los datos de un triángulo.

Implementar una clase con los métodos para inicializar los atributos,
imprimir el valor del lado con un tamaño mayor y el tipo de triángulo 
que es (equilátero, isósceles o escaleno).

'''
## Clases
class Triangulo:
	def __init__(self,lado1,lado2,lado3):
		self.lado1 = lado1
		self.lado2 = lado2
		self.lado3 = lado3
		self.ladoMayor = f"{self.calcularLadoMayor()} cm."
		self.tipo = self.calcularTipo() #equilátero, isósceles o escaleno

	def getLado1(self):
		return self.lado1
	def setLado1(self, nuevo):
		self.lado1 = nuevo
	def getLado2(self):
		return self.lado2
	def setLado2(self, nuevo):
		self.lado2 = nuevo
	def getLado3(self):
		return self.lado3
	def setLado3(self, nuevo):
		self.lado3 = nuevo

	def getLadoMayor(self):	
		return self.ladoMayor
	def getTipo(self):
		return f"Soy del tipo: {self.tipo}"


	def calcularLadoMayor(self):
		if self.lado1 >= self.lado2 and self.lado1 >= self.lado3:
			return self.lado1
		elif self.lado2 >= self.lado1 and self.lado2 >= self.lado3:
			return self.lado2
		elif self.lado3 >= self.lado1 and self.lado3 >= self.lado2:
			return self.lado3
		else:
			return None

	def calcularTipo(self):
		if self.lado1 == self.lado2 and self.lado1 == self.lado3:
			return "Equilatero"
		elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
			return "Isósceles"
		else:
			return "Escaleno"
	def __str__(self):
		return f"Soy un Triangulo de tipo: {self.tipo} y mi lado mayor mide: {self.ladoMayor}"



## Programa
'''
lado1 = input("Ingrese el tamaño del lado 1:")
lado2 = input("Ingrese el tamaño del lado 2:")
lado3 = input("Ingrese el tamaño del lado 3:")

triangulito = Triangulo(lado1,lado2,lado3)'''
t1 = Triangulo(18,23,12)
t2 = Triangulo(25,25,25)
t3 = Triangulo(25,25,10)

print("------------------------")
print(t1.getLadoMayor())
print(t1.getTipo())
print("------------------------")
print(t2.getLadoMayor())
print(t2.getTipo())
print("------------------------")
print(t3.getLadoMayor())
print(t3.getTipo())
print("------------------------")
print(f"{t1}\n{t2}\n{t3}\n")