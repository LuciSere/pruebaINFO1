'''
Puedes leer los elementos de la lista utilizando un ciclo for utilizando range():
>>> lista = ["a","b","c"]
>>> for index in range(0, len(lista)):
>>> print(lista[index])
a
b
c

recorrer listas de la siguiente manera
>>> lista = ["a","b","c"]
>>> for elemento in lista:
>>> print(elemento)

append()
>>> lista_de_compras = ["arroz", "harina", "huevo"]
>>> lista_de_compras.append("tomate")
>>> print(lista_de_compras)
["arroz", "harina", "huevo","tomate"]

insert()
series.insert(2, "Black Mirror")
>>> print(series)
["The IT Crowd", "Halt and Catch Fire", "Black Mirror", "Silicon Valley"]

extend() #agregar todos los elementos de otra lista al final 
>>> una_lista = ["Hola", 56, True, 3.44]
>>> otra_lista = ["A", 23, "B", "C"]
>>> una_lista.extend(otra_lista)
>>> print(una_lista)
['Hola', 56, True, 3.44, 'A', 23, 'B', 'C']
>>> print(otra_lista)
['A', 23, 'B', 'C']

Obtener sublistas (slicing)
a partir de una lista usando [ : ] de esta manera:
>>> mi_lista = ["a","b","c","d","e","f"]
>>> lista_cortada = mi_lista[1:3]
>>> print(lista_cortada)
['b', 'c']

El primer número indica el índice del primer elemento, y el segundo en donde
detenerse y dejar de tomar elementos.
>>> mi_lista = ["a","b","c","d","e","f"]
>>> mi_lista[3:5]
['d', 'e']
>>> mi_lista[0:6]
["a","b","c","d","e","f"]
Si se decide omitir el primer número, se comenzará desde el inicio.
>>> mi_lista[:4]
["a","b","c","d"]
mi_lista[:4] es igual a hacer mi_lista[0:4]
Si se elimina el segundo número se tomarán elementos hasta el final.
>>> mi_lista[0:]
["a","b","c","d","e","f"]
>>> mi_lista[4:]
['d', 'e', 'f']
mi_lista[3:] es igual a hacer mi_lista[3:len(lista)]
Ahora si no pones ningún número, y solo deja los dos puntos, se copiará la lista
completa.
>>> mi_lista[:]
["a","b","c","d","e","f"]
mi_lista[:] es igual a mi_lista[0:len(lista)]
Copiar un lista.
Si necesitamos una copia de la lista en otra variable podremos h
'''
