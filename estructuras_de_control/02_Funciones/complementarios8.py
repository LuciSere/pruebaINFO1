'''
Ejercicio 8: Capitalízalo
Muchas personas no usan letras mayúsculas correctamente, especialmente cuando 
escriben en dispositivos pequeños como teléfonos inteligentes. En este ejercicio,
 escribirá una función que capitaliza los caracteres apropiados en una cadena. 
Una "i" minúscula debe reemplazarse por una "I" mayúscula si está precedida y 
seguida de un espacio. El primer carácter de la cadena también debe estar en 
mayúscula, así como el primer carácter no espacial después de un ".", "!" o "?"
 Por ejemplo, si la función se proporciona con la cadena "¿a qué hora tengo que
 estar allí? ¿cuál es la dirección?" entonces debería devolver la cadena "¿A qué
 hora tengo que estar allí? ¿Cuál es la dirección?". Incluya un programa 
principal que lea una cadena del usuario, la capitalice utilizando su función 
y muestre el resultado.

funciones que existen:
.upper()#pone todo en mayus
.lowe()#pone todo en min
.capitalize()# en mayus la 1er letra del string y el resto en min
.swapcase()# lo que era min cambia a mayus y lo que era mayus cambia a min
.title() # cambia cada primer letra a mayus

booleanos
.islower()#si esta todo en min da true
.isupper()#si esta todo en mayus da true

'''
# Funciones
def capitalizar(string):#toma una cadena y coloca en mayusculas los caracteres que corresponde
	marca = 0
	string = string.capitalize()
	string2 = ""
	for char in string:
		if marca == 1:
			char = char.upper()
		if char == "¿" or char == "¡" or char == ".":
			marca = 1
		elif char == " " and marca == 1:
			marca = 1
		else:
			marca = 0			
		string2 += char 
	
	return string2


# Programa
cadena = input("Ingrse una cadena:\t")
resultado = capitalizar(cadena)
print("")
print(resultado)