'''Ejercicio 4: Mediana de tres valores
Escriba una función que tome tres números como parámetros y devuelva el valor 
medio de esos parámetros como resultado. Incluya un programa principal que lea 
tres valores del usuario y muestre su mediana.
Sugerencia: El valor medio es el medio de los tres valores cuando se ordenan en 
orden ascendente. Se puede encontrar usando declaraciones if, o con un poco de 
creatividad matemática.
#La mediana es un valor numérico que separa la mitad superior de un conjunto 
#de la mitad inferior. 
'''

def mediana(num1,num2,num3):
	if num1 <= num2 and num1 <= num3:#num1 es el menor	
		if num2 <= num3:
			valor = num2
		else:
			valor = num3
	elif num2 <= num1 and num2 <= num3:#num2 es el menor	
		if num1 <= num3:
			valor = num1
		else:
			valor = num3
	elif num3<= num2 and num3 <= num1:#num3 es el menor	
		if num2 <= num1:
			valor = num2
		else:
			valor = num1
	return valor

##con listas
#	aux = [num1,num2,num3]
#	aux.sort()# ordeno de menor a mayor
#	return aux[1]

#program
print("\nESTE PROGRAMA CALCULA LA MEDIANA DE TRES VALORES")
num1 = int(input("Ingrese el 1er num:\t"))
num2 = int(input("Ingrese el 2do num:\t"))
num3 = int(input("Ingrese el 3er num:\t"))
resultado = mediana(num1,num2,num3)
print(f"La mediana es: {resultado}")

