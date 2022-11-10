'''
Desafío 1
Escribir un programa que pregunte a diferentes personas cuánto conocen sobre
 contaminación del 1 al 10, almacene estos valores en una lista y los muestre
  por pantalla ordenados de menor a mayor. 
'''

lista = []
for persona in range(3):
	aux = int(input("¿cuánto conocen sobre contaminación del 1 al 10?:\t"))
	lista.append(aux)
lista.sort()
print(lista)