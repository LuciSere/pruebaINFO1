'''
A) Solicitar al usuario que ingrese numeros, los cuales se guardaran en una lista.
	Finaliza al ingresar 0, el cual no debe guardarse.
B)Solicitar al usuario que ingrese un numero y, si esta en la lista, elimine su primera ocurrencia.
	Mostrar un mje si no es posible eliminar.
C)Recorrer la lista para imprimir la sumatoria de todos los elementos.
D)Solicitar al usuario otro numero y crear una lista con los elementos de la lista original
	que sean menores que el numero dado. Imprimir esta nueva lista, iterando por ella.
E)Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos,
	cada una compuesta por un numero de la lista original y la cantidad de veces que aparece en ella
	Por ejemplo, dada la lista [5,16,2,5,57,5,2] la nueva lista contendra: [(5,3),(16,1),(2,2),(57,1)]
funciones primitivas usadas:

lista.remove(elto)# para eliminar el elemento dado de la lista
lista.count(elto)# para contar cuantas veces se repite un elemento en una lista
lista.append(elto)# para agregar un elemento a la lista

sum(lista) # para sumar los elementos de la lista

'''
## FUNCIONES
def menu(): # retorna una letra(convertida a mayus), la opcion elegida por el usuario
 	print("A - Ingresar numeros a la lista")
 	print("B - Eliminar numero de la lista")
 	print("C - Sumar numeros a la lista")
 	print("D - Mostrar los numeros de la lista que sean menores a un numero dado")
 	print("E - Tuplas, que muestren  el elemento y cantidad de apariciones")
 	print("\n--Para finalizar ingrese otra letra--\n")
 	letra = (input("Ingrese la opcion elegida:\t")).upper()
 	return letra

def hacer(opcion): #procedimiento que llama a la funcion segun la opcion dada, eimprime su resultado
	if opcion == "A":
		print(ingresar_numeros(lista))
	elif opcion == "B":
		print(eliminar_numero(lista))
	elif opcion == "C":
		print(sumar_numeros(lista))
	elif opcion == "D":
		print(mostrar_menores(lista))
	elif opcion == "E":
		print(mostrar_tuplas(lista))

def ingresar_numeros(lista):# Opcion A
	print("Digite el numero a ingresar. Para finalizar digite 0:")
	numero = int(input("\t"))
	while numero != 0:
		lista.append(numero)
		numero = int(input("\t"))
	return lista

def eliminar_numero(lista):# Opcion B
	numero = int(input("Digite el numero a eliminar:\t"))
	if numero in lista:
		lista.remove(numero)
	else:
		print(f"No se puede eliminar, \'{numero}\' no se encuentra en la lista")
	return lista

def sumar_numeros(lista):# Opcion C
	suma = 0 # otra forma seria:  print(sum(lista))
	for numero in lista:
		suma += numero
	return suma

def mostrar_menores(lista):# Opcion D
	numero = int(input("Ingrese un numero:\t"))
	menores = []
	for elto in lista:
		if elto < numero:
			menores.append(elto)
	return menores

def mostrar_tuplas(lista):# Opcion E
	lista_tuplas = []
	for elto in lista:
		tupla = (elto, lista.count(elto))
		if tupla not in lista_tuplas:
			lista_tuplas.append(tupla)
	return lista_tuplas



## PROGRAMA
print("\n¡Bienvenidos al programa para practicar listas!\n")
lista = [56, 14, 3, 87, 2, 5, 48, 69, 5, 2, 4, 17, 18, 9]
opciones = ["A","B","C","D","E"]
opcion = menu()
while opcion in opciones:
	print("------------------------------")
	hacer(opcion)
	print("------------------------------")
	print(f"\nLa lista actual es: {lista}\n")
	opcion = menu()
print("\nGracias por ulizar mi programa")

