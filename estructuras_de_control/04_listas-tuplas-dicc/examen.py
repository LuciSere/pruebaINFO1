'''
from random import shuffle
x = ["Tener", "El", "Azul", "Bandera", "Volar", "Alto"]

shuffle(x)
print(x)
'''
'''
#c.Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.
numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)
 '''
''' 
lista1 = [2, 33, 222, 14, 25]
print(lista1[-1])
'''




