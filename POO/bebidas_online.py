class Almacen():
	def __init__(self):
		self.lista_bebidas = []

	def agregar_bebida(self,bebida):
		test = isinstance(bebida,AguaMineral) or isinstance(bebida,Gaseosa)

		#Verificar tipo de dato
		if not test:
			raise Exception("Tipo de dato no permitido")

		#Verificamos id
		for b in self.lista_bebidas:# b es cada bebida dentro de la lista de bebidas
			if b.id == bebida.id:
				raise Exception("Id existente")
		self.lista_bebidas.append(bebida)

	def obtener_total(self,marca=None):
		total=0
		if marca is None:
			#Calculamos el precio total
			for b in self.lista_bebidas:
				total += b.get_precio()
		else:
			#Calculamos precio total de marca en particular
			for b in self.lista_bebidas:
				if b.marca == marca:
					total += b.get_precio()
		return total

	def eliminar_producto(self,id):
		x = None 
		for b in self.lista_bebidas:# b es cada bebida dentro de la lista de bebidas
			if b.id == bebida.id:
				self.lista_bebidas.append(bebida)

	def ver_info(self):
		for b in self.lista_bebidas:
			b.ver_info()

class Bebida():
	def __init__(self, id, ca_litros, marca, precio):
		self.id = id
		self.ca_litros = ca_litros
		self.marca = marca
		self.precio = precio

	def get_precio(self):
		return self.precio 

	def ver_info(self):
		print(f"ID: {self.id}")
		print(f"CANTIDAD DE LITROS: {self.ca_litros}")
		print(f"MARCA: {self.marca}")
		print(f"PRECIO: {self.precio}")

class AguaMineral(Bebida):
	def __init__(self, id, ca_litros, marca, precio, origen):
		super().__init__(id,ca_litros, marca, precio)
		self.origen = origen

	def ver_info(self):
		super().ver_info()
		print(f"ORIGEN: {self.origen}")
		
class Gaseosa(Bebida):
	def __init__(self, id, ca_litros, marca, precio, p_azucar, tiene_descuento):
		super().__init__(id,ca_litros, marca, precio)
		self.p_azucar = p_azucar
		self.tiene_descuento = tiene_descuento
		self.descuento = 0.1

	def get_precio(self):
		if self.tiene_descuento:
			return self.precio*(1-self.descuento)
		return self.precio 

	def ver_info(self):
		tiene = "Si" if self.tiene_descuento else "No"
		super().ver_info()
		print(f"PORCENTAJE DE AZUCAR: {self.p_azucar}%")
		print(f"TIENE DESCUENTO: {tiene}")
		print(f"DESCUENTO: {self.descuento}%")

###archivo "main.py" con las INSTANCIAS creadas

#from bebidas_online import Almacen, AguaMineral, Gaseosa

a = Almacen()

x = AguaMineral(id=1, ca_litros=2, marca="unaMarca", precio=12.3, origen="Manantial")
a.agregar_bebida(x)

y = AguaMineral(id=2, ca_litros=2, marca="otraMarca", precio=12.3, origen="Manantial")
a.agregar_bebida(y)

z = Gaseosa(id=3, ca_litros=1, marca="Marca X", precio=10, p_azucar=40, tiene_descuento=True)
a.agregar_bebida(z)

#a.eliminar_producto(2)

print(a.ver_info())

###PRUEBAS

print("\n----obtener_total----")
print(a.obtener_total(marca="Marca X"))

print("\n----ver_info----")
print(a.ver_info())