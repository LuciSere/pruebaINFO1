'''
Ejercicio 5: De número entero a número ordinal
Las palabras como primero, segundo y tercero se refieren a números ordinales. 
En este ejercicio, escribirá una función que toma un número entero como su único 
parámetro y devuelve una cadena que contiene el número ordinal apropiado como 
único resultado. Su función debe manejar los enteros entre 1 y 12 (inclusive). 
Debería devolver una cadena vacía si se proporciona un valor fuera de este rango 
como parámetro. Incluya un programa principal que utilice su función mostrando 
cada número entero del 1 al 12 y su número ordinal.
'''
def ordinal(numero):
	orden = ""#si no toma ninguno de los doce valores se quedara con este
	if numero == 1:
		orden = "Primero"
	elif numero == 2:
		orden = "Segundo"
	elif numero == 3:
		orden = "Tercero"
	elif numero == 4:
		orden = "Cuarto"
	elif numero == 5:
		orden = "Quinto"
	elif numero == 6:
		orden = "Sexto"
	elif numero == 7:
		orden = "Septimo"
	elif numero == 8:
		orden = "Octavo"	
	elif numero == 9:
		orden = "Noveno"
	elif numero == 10:
		orden = "Decimo"
	elif numero == 11:
		orden = "Undecimo o Decimo primero"
	elif numero == 12:
		orden = "Duodecimo o Decimo segundo"
	return orden

#programa
numero =int(input("\nIngrese un numero entre 1 y 12 para conocer su ordinal:\t"))
resultado = ordinal(numero)
print(f"El ordinal de {numero} es: {resultado}")