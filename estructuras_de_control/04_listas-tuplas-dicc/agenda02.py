"""Realizar una agenda, que se pueda guardar nombre y teléfono."""

#Funciones
#Función para opción 1: Buscar un contacto
def busca_contacto(diccionario):
	clave = input("Ingrese nombre de contacto\t")
	if clave in diccionario:
		op = input("Que dato desea buscar? \n1- Teléfono 1 \n2- Teléfono 2 \n3-Dirección\nIngrese:\t")
		v = diccionario[clave]
		if (op == "1"):
			clave_n = "Telefono1"
		elif(op == "2"):
			clave_n = "Telefono2"
		elif(op == "3"):
			clave_n = "Direccion"
		if clave_n in v:
			if (op == "1"):
				print(f"Nro de Teléfono 1 --> {v[clave_n]}")
			elif(op == "2"):
				print(f"Nro de Teléfono 2 --> {v[clave_n]}")
			elif(op == "3"):
				print(f"Dirección --> {v[clave_n]}")
			else:
				print("Opción ingresada incorrecta")								
			print("-----------------------------------------------------------------")
	else:
		print("Contacto Inexsistente")
		op = input("Desea agregar el contacto? 1 - Si 2 - No \n Ingrese:\t")
		if(op == "1"):
			agregar_contacto(diccionario)
		elif(op == "2"):
			print("Perfecto, consulta terminada!")
		else:
			print("Opción ingresada incorrecta")
		print("-----------------------------------------------------------------")

#Función para opción 2: Mostrar todos los contactos
def mostrar_agenda(diccionario):
	print("-----------------------------------------------------------------")
	for k,v in diccionario.items():
		print(f"Nombre --> {k} / {v}")
	print("-----------------------------------------------------------------")

#Función para opción 3: Agregar un contacto
def agregar_contacto(diccionario):
	nombre = input("Ingrese nombre de contacto\t")
	if nombre not in diccionario:
		numero1 = int(input("Ingrese número de teléfono\t"))
		op = input("Desea agregar un segundo número? 1- Si 2-No\n Ingrese:\t")
		if (op == "1"):
			numero2 = int(input("Ingrese el segundo número de teléfono\t"))
		else:
			numero2 = 0
		direccion= input("Ingrese una dirección\t")
		v = {}
		v["Telefono1"] = numero1
		v["Telefono2"] = numero2
		v["Direccion"] = direccion
		agenda[nombre] = v
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
		op = input(f"Que desea modificar del contacto {nombre}? \n1- Teléfono 1 \n2- Teléfono 2 \n3- Dirección \nIngrese:\t")		
		if (op == "1"):
			numero1 = int(input("Ingrese nuevo número de teléfono\t"))
			v = diccionario[nombre]
			v["Telefono1"] = numero1
		elif(op == "2"):
			numero2 =int(input("Ingrese el nuevo segundo número de teléfono\t"))
			v = diccionario[nombre]
			v["Telefono2"] = numero2
		elif(op == "3"):
			direccion= input("Ingrese nueva dirección\t")
			v = diccionario[nombre]
			v["Direccion"] = direccion
		else:
			print("Opción ingresada incorrecta")	
		print("-----------------------------------------------------------------")
		print("----------------Número de Contacto Modificado!!!-----------------")
	else:
		print("-----------------------------------------------------------------")
		print("El contacto que quiere modificar no existe")


def obtener_txt_como_diccionario(nombre_archivo):
	import ast
	separador = ","
	with open(nombre_archivo, encoding = "utf-8") as archivo:
		diccionario = {}
		for linea in archivo:
			linea =linea.rstrip("\n") #Quitar el salto de línea
			columnas = linea.split(separador)
			clave = columnas[0]
			valor = str(columnas[1] + ","  + columnas[2] + "," + columnas[3])
			valor = ast.literal_eval(valor)
			diccionario [clave] = valor
		return diccionario

def cargar_diccionario_a_archivo(nombre_archivo,diccionario):
	with open(nombre_archivo, "w") as arch:
		for k,v in diccionario.items(): 
			arch.write(f"{k},{v}\n")
		arch.close()
		return arch

#Programa
#Agenda inicial
#agenda = {"Renzo": {"Telefono1": 3624847841, "Telefono2" : 0, "Direccion": "Calle 1"}, "Maria": {"Telefono1": 36284845454, "Telefono2" : 0, "Direccion": "Calle 1"}, "Ayelen": {"Telefono1": 3432484215, "Telefono2" : 0, "Direccion": "Calle 1"}, "Mario": {"Telefono1": 654874544, "Telefono2" : 0, "Direccion": "Calle 1"}}

#Importo la agenda desde un archivo llamado data.txt
agenda = obtener_txt_como_diccionario("data2.0.txt")

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

#Exporto lo que hice en la variable agenda al archivo que se llama data.txt para mantener actualizado físicamente la agenda
archivo_actualizado = cargar_diccionario_a_archivo("data2.0.txt",agenda)

print("-----------------------------------------------------------------")
print("--------------Gracias por utilizar la Agenda---------------------")
print("-----------------------------------------------------------------")

