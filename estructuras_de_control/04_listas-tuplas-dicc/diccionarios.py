'''
lista de listas
[[nombre, numero],[nombre, numero]]
lista de tuplas
[(nombre, numero),(nombre, numero)]

diccionarios: {clave:valor, clave:valor}
valor: puede ser cualquier cosa
ej
{nombre: numero, nombre: numero}

'''
'''
agenda = {} #es un diccionario

#agenda[clave] = valor # para asignar

agenda["nico"] = 3624010101
agenda["marta"] = 3624020202
agenda["maria"] = 3624030303
agenda["abel"] = 3624040404

#las claves no se pueden repetir, 
#si la clave no existe la crea, y le asigna valor
#si la clave ya existe modifica el valor

#NOS RETORNA LAS CLAVES agenda.keys()
#NOS RETORNA LOS VALORES agenda.values()
#NOS RETORNA CADA PAR CLAVE VALOR COMO UNA TUPLA agenda.item()

print(agenda)
print("")

#esto solo me muestra las claves
#for elemento in agenda:
#	print(elemento)

#[(nombre, numero),(nombre, numero)] ----> esto es agenda.items()

for x in agenda.items():
	print(f"{x[0]} --> {x[1]}")

for clave,valor in agenda.items(): #nos permite nombrar alos elementos asi clave,valor.
	print(f"{clave} --> {valor}")

#para cargar un nuevo item
nombre = input("Ingrese NOMBRE: \t")
numero = int(input("Ingrese NNUMERO: \t"))

agenda[nombre] = numero


#Otro ejemplo: guardar info de los estudiantes, nombre, dni, sexo, edad

{
	dni: [nombre, sexo, edad],
	dni: [nombre, sexo, edad]
}
{
	dni: {"nombre": nombre, "sexo": sexo, "edad": edad},
	dni: {"nombre": nombre, "sexo": sexo, "edad": edad},
}
'''

estudiante = {}

for i in range(3):
	dni = input("DNI:\t")
	nombre = input("Nombre:\t")
	sexo = input("sexo:\t")
	edad = input("edad:\t")

	cada_uno = {}
	cada_uno["nombre"] = nombre
	cada_uno["sexo"] = sexo
	cada_uno["edad"] = edad
	#OTRA FORMA DE HACER LO MISMO:
	#cada_uno = {"nombre": nombre, "sexo": sexo, "edad": edad}

	estudiante[dni] = cada_uno
print(estudiante)
print("")

for k, v in estudiante.items():
	print(f"ESTUDIANTE DNI:{k}")
#	print(f"VALORES: {v}")	#hasta aca una opcion, sino la que sigue, sin esta linea
	for x,i in v.items():
		print(f"{x} --> {i}")


