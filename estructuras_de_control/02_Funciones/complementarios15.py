'''
Ejercicio 15: Verificar una contraseña
En este ejercicio escribirá una función que determina si una contraseña es 
buena o no. Definiremos como una buena contraseña aquella que tenga una longitud
 de al menos 8 caracteres y contenga al menos una letra mayúscula, al menos una 
letra minúscula y al menos un número. Su función debe devolver verdadero si la 
contraseña que se le pasó, como único parámetro, es buena, de lo contrario 
debería devolver falso. Incluya un programa principal que lea una contraseña del
 usuario e informe si es buena o no.
'''

def contasenia_adecuada(contrasenia):
 	num = 0
 	mayus = 0
 	minuscula = 0
 	for letra in contrasenia:
 		ascci = ord(letra)
 		if (ascci >= 48  and ascci <= 57):
 		 	num += 1
 		elif(ascci >= 65  and ascci <= 90):
 		 	mayus += 1
 		elif(ascci >= 97  and ascci <= 122):
 		 	minuscula += 1
 	longitud = len(contrasenia)> 7
 	return (num > 0)  and (minuscula > 0)  and (mayus > 0) and longitud


# programa
contrasenia = input("Ingrese una contraseña:\t")

buena = contasenia_adecuada(contrasenia)

print("¿Es segura la contraseña?\t", buena)
