'''
[] listas
() tuplas
{} dicc

mi_lista ={} #creo una lista vacia
mi_lista = list() #asigno una lista vacia a mi varivle. a fines practicos es lo mismo
.append() #para agregar un elemento al final de la lista
.index()
.sort() #para ordenar la lista
len() #para contar los elemntos de la lista. el 1er elemento es la lposicion 0
x[1:4] #muestro una parte de la lista, inicia en el numero(que indica el indice) antes de los 2 puntos, y finaliza en el anterior indice al indicad despues de los 2 puntos. 
reverse #dar vuelta el orden de los elementos 

lista1.sort(reverse = True)#ordenadirectamente al revez de mayor a menor.
lista1.reverse() #cambio el orden. el ultimo elemento va ser el primeroy asi
lista.extend(elemento) # agrega un elemento mas a la lista

'''
'''
mi_lista =[]

for i in range(5):
	n = int(input("ingrese un numero:\t"))
	mi_lista.append(n)

mi_lista.sort()
print(mi_lista)
print(mi_lista[2]) #imprimo un elemnteo, indique la posicion
for x in mi_lista:
	print(f"Elemnto {x}")

x = [2,3,7,8,1,5]
y = [2,"nico",50]
z = [2,[1,2,3],[8,7]] #lista que contiene otras listas como elementos

for i in x[1:4]:
	print(i)

'''


notas = [[5,6,7],[10,9,8],[3,5,6]]

for i in notas:
	# i en la primer vuelta vale [5,6,7]
	# i en la segunda vuelta vale [10,9,8]
	# i en la tercer vuelta vale [3,5,6]
	prom = sum(i)/len(i) #saco el promedio de i
	print(f"El promedio de este alumno es:  {round(prom,2)}")
