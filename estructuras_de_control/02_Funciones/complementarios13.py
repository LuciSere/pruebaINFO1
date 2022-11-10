'''
Ejercicio 13: Contraseña aleatoria
Escriba una función que genere una contraseña aleatoria. La contraseña debe tener
 una longitud aleatoria de entre 7 y 10 caracteres. Cada carácter debe 
seleccionarse al azar de las posiciones 33 a 126 en la tabla ASCII. Su función 
no tomará ningún parámetro y devolverá la contraseña generada aleatoriamente 
como su único resultado. Desarrolle un programa principal y muestre la contraseña
 generada aleatoriamente.
Sugerencia: Probablemente encuentre útil la función chr( un num a un valor ascci) cuando complete este 
-aleatorios entre 33
ejercicio.
-genero un numero random para la longitud
-con esa longitud hago un ciclo for
- creo una variable cadena
- dentro del for:
	-generar un numero random o azar entre 33 y 126
	-convertir el numero a ascci con la funcion chr
	-guardarlo como cadena en la variable cadena
- imprimir la cadena
'''
import random

def contrasenia_aleatoria():
	longitud = random.randint(7,10)
	cadena = ""
	for i in range(1,longitud+1,1):
		numero = random.randint(33,126)
		assi= chr(numero)
		cadena = cadena + assi
	return cadena

# programa

contrasenia = contrasenia_aleatoria()
print(contrasenia)

