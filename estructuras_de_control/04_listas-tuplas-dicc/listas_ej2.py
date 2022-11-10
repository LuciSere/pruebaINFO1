'''
se tiene una lista con los datos de clientes de una compañia de telefonia celular, 
los cuales pueden aparecer repartidos en la lista si tiene registrado mas de un numero telefonico
La compañia para su proximo aniversario desea enviarles un regalo a cada numero registrado sin repetir regalos por cliente
en una lista se almacenan los regalos disponibles en orden.
se desea un programa que cree una nueva lista con los clientees, sin repeter i y ordenada
Y al final muestre el regalo quele corrresponde a cada cliente
'''
### Funciones
def cargar_clientes(lista):
	for i in range(30):
		lista.append(random.randint(1,12))
	return lista

def depurar(lista):
	lista2 = []
	for elto in lista:
		if elto not in lista2:
			lista2.append(elto)
	lista2.sort()# ordeno
	return lista2

def repartir_regalos(clientes,clientes_solo):
	regalos = ["Regalo 1","Regalo 2","Regalo 3"]

	for elto in clientes_solo:
		print(f"\nCliente: {elto}, que tiene {clientes.count(elto)} cuenta/s\n")
		regalito = 0
		print("\tRecibe : ", end="")
		while (regalito < clientes.count(elto)) and (regalito <= len(regalos)-1):
			print(regalos[regalito]," ", end="")
			regalito += 1
		print("")


### Programa
clientes = []
import random
clientes = cargar_clientes(clientes)
print("Clientes sin depurar: ", clientes)
clientes_solo = depurar(clientes)
print("Clientes depurado: ", clientes_solo)

repartir_regalos(clientes,clientes_solo)




