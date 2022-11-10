
'''
https://sites.google.com/view/informatorio-poo/level-stone?authuser=0
Caso 4
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el
 nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes 
 opciones.

Añadir contacto
Lista de contactos
Buscar contacto
Editar contacto
Cerrar agenda

clase agenda tiene un atributo que es la lista de contactos
'''
## CLASES

class Agenda:
	def __init__(self, listaContactos):
		self.contactos = listaContactos
	
	def mostrar(self):
		for i in self.contactos:
			print(i.__str__())

	def buscar(self, nombre_contacto):
		lista = self.contactos
		for contac in lista:
			if contac.nombre == nombre_contacto:
				return contac
				break
			else:
				pass
		else:
			return None

	def agregarContacto(self, contacto):
		self.contactos.append(contacto)


class Contacto:
	def __init__(self, nombre, telefono, email):
		self.nombre = nombre 
		self.telefono = telefono
		self.email = email

	def getNombre(self):
		return self.nombre
	def setNombre(self, nuevo_nombre):
		self.nombre = nuevo_nombre
	
	def getTelefono(self):
		return self.telefono
	def setTelefono(self, nuevo_tel):
		self.telefono = nuevo_tel
	
	def getEmail(self):
		return self.email
	def setEmail(self, nuevo_email):
		self.email = nuevo_email

	def __str__(self):
		return f"Nombre: {self.getNombre()}. Teléfono: {self.getTelefono()}. Email: {self.getEmail()}"

### FUNCIONES
def opcion():# muestra el menu y retorna la opcion elegida por el usuario
 	opciones = ["1","2","3","4","5"]
 	print("----------------MENU------------------")
 	print("\t1 - Añadir contacto\n\t2 - Lista de contactos\n\t3 - Buscar contacto\n\t4 - Editar contacto\n\t5 - Cerrar agenda\n")
 	opcion = input("Ingrese un numero: ")
 	while (opcion not in opciones):
 		opcion = input("Opcion incorrecta. Ingrese nuevamente: ")

 	return opcion

def hacer(opcion, agenda): #Ejecuta la accion elegida
	if opcion == "1":#Añadir contacto
		nuevoContacto(agenda)
	if opcion == "2":#Lista de contactos
		agenda.mostrar()
	if opcion == "3":#Buscar contacto
		buscarContacto(agenda)	
	if opcion == "4":#Editar contacto
		editarContacto(agenda)
		
def nuevoContacto(agenda):
	nombre = input("Ingrese nombre:\t").upper()
	tel = input("Ingrese teléfono:\t")
	email = input("Ingrese Email:\t")
	contacto = Contacto(nombre,tel,email)
	agenda.agregarContacto(contacto)
	print("Contacto guardado")

def buscarContacto(agenda):# si lo encuentra retorna el str y si no dice no encontrado
	nombre_buscar = ((input("Ingrese el nombre del contacto:\t")).upper())
	encontrado = agenda.buscar(nombre_buscar)
	if encontrado == None:
		print("Contanto no encontrado")
	else:
		print(encontrado)
	return encontrado

def editarContacto(agenda):
	encontrado = buscarContacto(agenda)
	if encontrado != None:
		while True:
			print("Que desea modifiacar:\n1-Nombre\n2-Telefono\n3-Email")
			opcion = input()
			if opcion == "1":
				nuevo_nombre = (input("Ingrese el nuevo Nombre:\t")).upper()
				encontrado.setNombre(nuevo_nombre)
				print("El Nombre se ha modificado y guardado.")
			elif opcion == "2":
				nuevo_telefono = input("Ingrese el nuevo Telefono:\t")
				encontrado.setTelefono(nuevo_telefono)
				print("El Telefono se ha modificado y guardado.")
			elif opcion == "3":
				nuevo_email = input("Ingrese el nuevo Email:\t")
				encontrado.setEmail(nuevo_email)
				print("El Email se ha modificado y guardado.")
			else:
				print("Opcion incorrecta.")
			if (input("desea realizar otra modificacion, al mismo contacto? s/n:\t")).upper() == "N":
				break
		


#menu
#### PROGRAMA

print("BIENVENIDO AL PROGRAMA AGENDA")
c1= Contacto("LUCI","454545","bla@gmail.com")
c2= Contacto("MATI","398723","ble@gmail.com")
c3= Contacto("LEO","2037787","bli@gmail.com")
agenda = Agenda([c1,c2,c3])

while True:
	op = opcion() # muestra el menu y retorna la opcion elegida por el usuario
	if op == "5":#cerrar agenda
		break
	else:
		hacer(op, agenda)# ejecuta la opcion elegida
		print("--------------------------------------")	
print("Fin")



