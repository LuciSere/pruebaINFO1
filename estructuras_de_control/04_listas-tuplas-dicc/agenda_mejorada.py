'''
agenda hecha con listas, diccionarios, funciones, un menu
+agregar: nombre, tel, dir 
+agregar elemento
el menu debe permitir: 
	+agregar elemento
	buscar un nombre
	buscar un tel
	listar toda la agenda
	modificar un numero
'''
#funciones


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
		nombre = input("Ingrese el nombre del contacto a buscar:\t")
		if nombre not in agen:
			print(f"El contacto {nombre} no fue encontrado")
		else:
			print(f"\n{agen[nombre]}\n")#imprime toda la info del contacto

		if input("Desea buscar otro contacto? (s/n):\t") == "n":
			break

def buscar_tel(dic):#Opcion 3
	while True:
		tel = input("Ingrese el telefono:\t")
		marca = 0 
		for nombre, datos in dic.items():#nombre{}
			for k, v in datos.items():#tel:485758,
				if tel in v:
					print(nombre, datos) #imprime toda la info del contacto
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
		nombre = input("Ingrese el nombre del contacto:\t")
		if nombre not in dic:
			print(f"El contacto {nombre} no fue encontrado")
		else:
			del dic[nombre]
			print(f"El contacto {nombre}, ha sido eliminado")

		if input("Desea eliminar otro contacto? (s/n):\t") == "n":
			break

def menu(opcion, agen):#ejecuta la opcion elegida
	if opcion == 1:
		cargar_contacto(agen)
	elif opcion == 2:
		buscar_nombre(agen)
	elif opcion == 3:
		buscar_tel(agen)
	elif opcion == 4:
		modificar_contacto(agen)
	elif opcion == 5:
		mostrar_agenda(agen)
	elif opcion == 6:
		eliminar_contacto(agen)	
	else:
		print("Opcion incorrecta")

#programa

agenda = {
	"Lu":{'TELEFONO': '3456', 'DIRECCION': 'calle 123'},
	"Mar":{'TELEFONO': '123654', 'DIRECCION': 'Calle 222'},
	"Fede":{'TELEFONO': '65546', 'DIRECCION': 'Calle 333'}
}
print("Este programa es una agenda de contactos. Elija la opcion a realizar:")
while True:
	print("\t1 - Ingresar un contacto")
	print("\t2 - Buscar un contacto por nombre")
	print("\t3 - Buscar un contacto por telefono")
	print("\t4 - Modificar un contacto")
	print("\t5 - Mostrar toda la agenda")
	print("\t6 - Eliminar un contacto")
	print("\t7 - Salir")
	opcion = int(input("Ingrese numero de opcion:\t"))
	print("")
	if opcion == 7:
		break	#salir
	else:
		menu(opcion, agenda)
	print("---------------------------------------------")
print("Gracias por utilizar mi programa")

