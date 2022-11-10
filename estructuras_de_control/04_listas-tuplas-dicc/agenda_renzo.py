"""Realizar una agenda, que se pueda guardar nombre y teléfono."""

#Funciones
#Función para opción 1: Buscar un contacto
def busca_contacto(diccionario):
	clave = input("Ingrese nombre de contacto\t")
	if clave in diccionario:
		print(f"Nro de Teléfono --> {diccionario[clave]}")
		print("-----------------------------------------------------------------")
	else:
		print("Contacto Inexsistente")
		print("-----------------------------------------------------------------")

#Función para opción 2: Mostrar todos los contactos
def mostrar_agenda(diccionario):
	print("-----------------------------------------------------------------")
	for k,v in diccionario.items():
		print(f"Nombre --> {k} / Teléfono --> {v}")
	print("-----------------------------------------------------------------")

#Función para opción 3: Agregar un contacto
def agregar_contacto(diccionario):
	nombre = input("Ingrese nombre de contacto\t")
	if nombre not in diccionario:
		numero = int(input("Ingrese número de teléfono\t"))
		agenda[nombre] = numero
		print("----------------------Contacto Agregado!!!!----------------------")
	else: 
		op = input("Contacto Existente Desea Modificar el número de teléfono? 1- Si 2- No \n Ingrese:\t")
		if (op == "1"):
			modificar_contacto(nombre,diccionario)
		else:
			print("No se ha modificado ningún usuario existente")

#Función para opción 4: Eliminar un contacto
def eliminar_contacto(diccionario):
	nombre = input("Ingrese el nombre de contacto que quiere eliminar\t")
	if nombre in diccionario:
		del diccionario[nombre]
		print("-----------------------------------------------------------------")
		print("-----------------------Contacto Eliminado!!!---------------------")
	else:
		print("-----------------------------------------------------------------")
		print("Contacto Inexsistente")


#Función para opción 5: Modificar número de contacto
def modificar_contacto(nombre,diccionario):
	if nombre in diccionario:
		numero = int(input("Ingrese nuevo número de teléfono\t"))
		diccionario[nombre] = numero
		print("-----------------------------------------------------------------")
		print("----------------Número de Contacto Modificado!!!-----------------")
	else:
		print("-----------------------------------------------------------------")
		print("El contacto que quiere modificar no existe")

#Programa
#Agenda inicial
agenda = {"Renzo": 3624847841, "María": 36284845454, "Ayelén": 3432484215, "Mario": 654874544}

print("-----------------------------------------------------------------")
print("---------------------Bienvendos a la Agenda----------------------")
print("-----------------------------------------------------------------")
while True:
	op = input("Que quieres hacer? \n 1- Buscar un contacto \n 2- Mostrar todos los contactos \n 3- Agregar un contacto \n 4- Eliminar un contacto \n 5- Modificar número de contacto existente \n Ingrese:\t")
	print("-----------------------------------------------------------------")
	if (op == "1"):
		print("---------------------Buscar Un Contacto--------------------------")
		busca_contacto(agenda)
		print("-----------------------------------------------------------------")
	elif(op == "2"):
		print("------------------------Lista de Contactos---------------------- ")
		print("")
		mostrar_agenda(agenda)
		print("")
		print("-----------------------------------------------------------------")
	elif(op == "3"):
		print("------------------Agregar un contacto---------------------")		
		agregar_contacto(agenda)
		print("-----------------------------------------------------------------")
	elif(op == "4"):
		print("--------------------Eliminar Un contacto-------------------")		
		eliminar_contacto(agenda)
		print("-----------------------------------------------------------------")
	elif(op == "5"):
		print("---------------Modificar Número de Contacto----------------")
		nombre = input("Ingrese el nombre de contacto que quiere modificar\t")
		modificar_contacto(nombre,agenda)
		print("-----------------------------------------------------------------")
	else:
		print("-----------------------------------------------------------------")
		print("Opción ingresada incorrecta")		
		print("-----------------------------------------------------------------")
	desicion = input("Desea Continuar? 1 - Si 2 - No \n Ingrese:\t")
	if (desicion == "2"):
		break
	print("-----------------------------------------------------------------")
print("-----------------------------------------------------------------")
print("--------------Gracias por utilizar la Agenda---------------------")
print("-----------------------------------------------------------------")

