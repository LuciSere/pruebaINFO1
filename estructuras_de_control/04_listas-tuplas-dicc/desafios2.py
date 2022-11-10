'''
Desafío 2	
Crea una tupla con los factores que más afectan a los mares. Luego para jugar con
niños y niñas, aprendiendo sobre contaminación del agua crea un programa que 
pida números, si el numero esta entre 1 y la longitud máxima de la tupla, 
muestra el contenido de esa posición sino muestra un mensaje de error.

El programa termina cuando el usuario introduce un cero.
'''
tupla = ("","sfr","a","e","f")
while True:
	num = int(input("Ingrese un numero:\t"))
	if num >= len(tupla):
		print("Error. en numero ingresado esta fuera de rango.")
	elif num == 0:
		break
	else:
		print(tupla[num])
print("Fin del programa.")