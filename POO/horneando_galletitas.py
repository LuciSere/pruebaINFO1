'''
Se corresponde con el video explicativo de POO
-ejemplos de aplicacion: parte 3
en el video se llama metodo.py
'''
class Galletita:
	sabor = "Vainilla"
	cantidad = 0

	def __init__(self):
		self.decoracion = False
		Galletita.cantidad += 1
		print("He cocinado una galletita")

	def hornear(self):
		print("Ya estoy horneada")
		print(self)

	def cambiar_sabor(self):
		self.sabor = "Chocolate"

	def __str__(self):
		return f"Esta es la galletita numero {Galletita.cantidad}"

	def retornar_decoracion(self):
		return self.decoracion
###pruebas
print("---creando intancias(objetos) e imprimiendo el constructor __init__ automaticamente---")
galle1 = Galletita()
galle2 = Galletita()
galle3 = Galletita()

print("\n---imprimiendo el self ---")
galle1.hornear()

print("\n---cambiando el sabor---")
print(galle2.sabor)
galle2.cambiar_sabor()
print(galle2.sabor)

print("\n---imprimiendo el  __str__ (contiene el atributo de clase: cantidad galletitas), \ncreando otra intancia y volviendo a imprimir el str---")
print(galle3)
galle4 = Galletita()
print(galle4)

print("\n---retornando el atributo (de objeto): decoracion ---")
print(galle3.retornar_decoracion())

