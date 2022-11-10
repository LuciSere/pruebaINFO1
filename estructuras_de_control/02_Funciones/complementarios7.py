'''
Ejercicio 7 : ¿Es un triángulo válido?
Si tiene 3 varillas, posiblemente de diferentes longitudes, puede o no ser 
posible colocarlas para que formen un triángulo cuando sus extremos se toquen. 
Por ejemplo, si todas las varillas tienen una longitud de 6 centímetros. 
entonces uno puede construir fácilmente un triángulo equilátero con ellos. 
Sin embargo, si una varillas es de 6 centímetros de largo, mientras que los 
otros dos son cada uno de solo 2 centímetros de largo, entonces no se puede 
formar un triángulo. 
En general, si una longitud es mayor o igual que la suma de las otras dos, 
entonces las longitudes no pueden usarse para formar un 
triángulo. De lo contrario, pueden formar un triángulo.
 Escriba una función 
que determine si tres longitudes pueden formar un triángulo. La función tomará
 3 parámetros y devolverá un resultado booleano. Además, escriba un programa 
que lea 3 longitudes del usuario y muestre el comportamiento de esta función.
'''
def puede_triangulo(lado1, lado2, lado3):
	mayor = 0
	if lado1 >= lado2 and lado1>= lado3:#lado1 es el mayor o es igual a uno o 2 de los lados
		mayor = lado1
	elif lado2 >= lado1 and lado2>= lado3:#lado1 es el mayor
		mayor = lado2
	elif lado3 >= lado1 and lado3>= lado2:#lado1 es el mayor
		mayor = lado2
	menores = (lado1 + lado2 + lado3) - mayor
	if mayor >= menores:
		resultado = False 
	else:
		resultado = True
	return resultado

#--Programa--
print("Este programa le dira si puede formar un triangulo con tres varillas:")
lado1 =float(input("Ingrese la longitud de la primer varilla"))
lado2 =float(input("Ingrese la longitud de la segunda varilla"))
lado3 =float(input("Ingrese la longitud de la tercer varilla"))
resultado = puede_triangulo(lado1,lado2,lado3)
print(f"puede crear un triangulo?: {resultado}")
