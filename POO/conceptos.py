'''
puedo usar parametros por defecto en el objeto(ejemplo: marca) y tambiene en las funciones
#todos los self. son los atributos
#los def son los metodos, y se escriben iguala funciones, son funciones

# no todos los atributos va estare en el paramertro(ej: precio_por_mayor)


'''
class Producto:
	#se ejecuta siempre al crear un objeto
	def __init__(self, nom, prec, sto, marca = '0'):
		self.nombre = nom#todos estos self. son los atributos
		self.precio = prec
		self.stock = sto
		self.precio_por_mayor = self.precio * 0.8
		self.marca = ""

	def mostrar_nombre(self):# y todos estos def son los metodos, y se escriben iguala funciones, son funciones
		print(f"Mi nombre es {self.nombre}")

	def mi_stock(self):
		print(f"Mi stock es {self.stock}")

	def cambiar_stock(self,nuevo):
		self.strock = nuevo

	def mostrar_precio(self):
		print(f"Mi preciopor menor es {self.precio}\n mi precio por mayor es {self.precio_por_mayor}")

	def cambiar_marca(self, nuevo):
		self.marca = nuevo

	def mostrar_marca(self):
		print(f"Mi marca es {self.marca}")	

#AFUERA

p1 = Producto("Yerba", 100, 50)
p1 = Producto("Leche", 150, 10)

p1.motrar_nombre()# "Mi nombre es Yerba"

#ENCAPSULADO
p1.cambiar_marca("Rosamonte")# el unico responsable de cambiar es la clase
#SIN ENCAPSULAR --->NO RECOMENDABLE
p1.marca = 'Playadito'#estoy haciendo por fuera de la clase

p1.mostrar_marca()
