'''
carge dos listas, y actualice la 1era con los elewmentos de la segunda
conceptitos: 
lista1.sort()#ordena la lista de menor a mayor
print(lista1)
lista1.sort(reverse = True)#ordenadirectamente al revez de mayor a menor.
lista1.reverse() #cambio el orden. el ultimo elemento va ser el primeroy asi
print(lista1)
lista.extend(elemento) # agrega un elemento mas a la lista

las tuplas a diferencia de las listas no cambia.
'''
import random # para que funcione random.randint(a,b)

lista1 = []
lista2 = []
for i in range(10):
	lista1.append(random.randint(1,10)) #agregue un numero aleatorio entre 1 y 10 a la lista1
	lista2.append(random.randint(1,10))
print(lista1)
print(lista2)

#busco si cada elemento esta en la lista 1, si no esta lo agrego.
for elto in lista2:
 	if elto not in lista1: #con en in, se fija los elementos de toda la lista
 		print(f"Se agrego el elemento: {elto}")
 		lista1.append(elto)
print(lista1)
