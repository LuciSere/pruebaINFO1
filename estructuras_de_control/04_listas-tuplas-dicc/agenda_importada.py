# relacione al archivo contactos_agenda.txt

def cargar_contacto(agen):#Opcion 1
	while True:
		nombre = input("NOMBRE:\t")
		tel = input("TELEFONO:\t")
		direccion = input("DIRECCION:\t")
		contacto = {"TELEFONO":tel,"DIRECCION":direccion}
		agen[nombre] = contacto
		print("\n\tEl contacto fue agregado\n")
		if input("Desea agregar otro contacto? (s/n):\t") == "n":
			break

def buscar_nombre(agen):#opcion2
	while True:
		buscar = input("Ingrese el nombre del contacto a buscar:\t")
		if buscar not in agen:
			print(f"El contacto {buscar} no fue encontrado")
		else:
			print(f"\n{agen[buscar]}\n")#imprime toda la info del contacto
		if input("Desea buscar otro contacto? (s/n):\t") == "n":
			break

def buscar_tel(dic):#Opcion 3
	while True:
		tel = input("Ingrese el telefono:\t")
		marca = 0 
		for nombre, datos in dic.items():#nombre{}
			for k, v in datos.items():#tel:485758,
				if tel in v:
					print(nombre, datos) #implime toda la info del contacto
					marca = 1
					break
				else:
					marca = 0
			if marca == 1:
				break
		if marca == 0:
			print(f"El telefono {tel} no fue encontrado")
		if input("Desea buscar otro contacto? (s/n):\t") == "n":
			break

def modificar_contacto(dic):#Opcion 4
	while True:
		nombre = input("Ingrese el nombre del contacto a modificar:\t")
		if nombre not in dic:
			print(f"El contacto {nombre} no fue encontrado")
		else:
			print(dic[nombre])
			opcion = input("Que deseamodificar?\n\t 1- TELEFONO\n\t 2- DIRECCION\n")
			if opcion == "1":
				tel = input("Ingrese el nuevo telefono:\t")
				#dic{nombre{telefono:tel}}
				dic[nombre]["TELEFONO"] = tel
			elif opcion == "2":
				direccion = input("Ingrese la nueva direccion:\t")
				dic[nombre]["DIRECCION"] = direccion
			else:
				print("Opcion incorrecta")
		if input("Desea modificar otro contacto? (s/n):\t") == "n":
			break		

def mostrar_agenda(dic):#Opcion 5
	for k, v in dic.items():
		print(f"{k}: {v}")

def eliminar_contacto(dic): #Opcion 6
	while True:
		buscar = input("Ingrese el nombre del contacto:\t")
		if buscar not in dic:
			print(f"El contacto {buscar} no fue encontrado")
		else:
			del dic[buscar]
			print(f"El contacto {buscar}, ha sido eliminado")
		if input("Desea eliminar otro contacto? (s/n):\t") == "n":
			break

def menu(opcion):#ejecuta la opcion elegida
	if opcion == 1:
		cargar_contacto(agenda)
	elif opcion == 2:
		buscar_nombre(agenda)
	elif opcion == 3:
		buscar_tel(agenda)
	elif opcion == 4:
		modificar_contacto(agenda)
	elif opcion == 5:
		mostrar_agenda(agenda)
	elif opcion == 6:
		eliminar_contacto(agenda)

def importar_contactos(archivo):
	import ast
	with open(archivo, encoding = "utf-8") as file:
		diccionario = {}
		for linea in file:
			linea = linea.rstrip("\n")# toma hasta el salto de linea
			columna = linea.split(",")# este es el separador de columnas
			clave = columna[0]
			aux = columna.pop(0) # aca elimine el 1er columna
			valor = ""
			for i in columna:
				bandera = False
				for x in i:
					if x == "}":
						bandera = True
				if bandera:
					valor = valor + i 
				else:
					valor = valor + i + ","

			valor = ast.literal_eval(valor)
			diccionario[clave] = valor
		file.close()
		return diccionario

def guardar_agenda(diccionario, archivo):
	with open(archivo, "w") as file: #esto reescribe el txt
		for k,v in diccionario.items():
			file.write(f"{k},{v}\n")
		file.close()
		return file

#programa

'''agenda = {
Lu,{'TELEFONO': '3456', 'DIRECCION': 'calle 123'}
Mar,{'TELEFONO': '123654', 'DIRECCION': 'Calle 222'}
Fede,{'TELEFONO': '65546', 'DIRECCION': 'Calle 333'}
Nico,{'TELEFONO': '56565', 'DIRECCION': '777'}
Luli,{'TELEFONO': '424242', 'DIRECCION': '7888'}
}'''

agenda = importar_contactos("contactos_agenda.txt")

print("\nEste programa es una agenda de contactos. Elija la opcion a realizar:")
while True:
	print("\t1 - Agregar un contacto")
	print("\t2 - Buscar un contacto por nombre")
	print("\t3 - Buscar un contacto por telefono")
	print("\t4 - Modificar un contacto")
	print("\t5 - Mostra toda la agenda")
	print("\t6 - Eliminar un contacto")
	print("\t7 - Salir")
	opcion = int(input("\nIngrese numero de opcion:\t"))
	print("")
	if opcion == 7:
		break	#salir
	else:
		menu(opcion)
	print("---------------------------------------------")

guardar_agenda(agenda, "contactos_agenda.txt")
print("Gracias por utilizar mi programa")

