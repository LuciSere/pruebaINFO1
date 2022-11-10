
'''
1) Determinar el número mayor de 10 números ingresados.
'''
'''
numeroMayor = 0
for i in range(10):
	numeroIngresado = int(input("ingrese un numero: \t"))
	if numeroIngresado> numeroMayor:
		numeroMayor = numeroIngresado
print(f"El numero mayor ingresado es: {numeroMayor}")
'''
'''

3) Diseñar un programa que permita obtener el producto 
entre A y B mediante sumas sucesivas.
'''
'''
a = 2
b = 3
total = 0
for i in range(b):
	total = total + a
print(f"el total es: {total}")
'''
'''
8) Diseñar un programa que permita calcular 
el total de una compra, ingresando cantidad y
precio de los productos. El programa debe estar
preparado para que el ingreso de los datos se
produzca hasta que el usuario lo desee.
'''


total = 0
while (True):
	precio = int(input("ingrese el precio del producto:\t"))
	cantidad = int(input("ingrese la cantidad:\t"))
	total = total + (precio * cantidad)
	continuar = input("Desea ingresar mas productos? si/no: \t")
	if continuar == "no":
		break
print(f"El total es: {total}")