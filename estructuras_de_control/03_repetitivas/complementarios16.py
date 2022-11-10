
'''
16) Escribir un programa el cual lea dos valores enteros. 
Si el primero es menor que el segundo, que imprima el mensaje ``Arriba''. 
Si el segundo es menor que el primero, que imprima el mensaje ``Abajo''. 
Si los números son iguales, que imprima el mensaje ``igual''. 
Si alguno de los datos ingresados es igual a 0, que imprima un mensaje conteniendo 
la palabra ``Error''.
'''
#while paraa que sea repetitiva
while(True):
	#lea 2 valores enteros
	num1 = int(input("ingrese el 1er numero:\t"))
	num2 = int(input("ingrese el 2er numero:\t"))
	print("---------------------")
	#si son iguales "igual"
	if num1 == num2:
		print("Igual")
	#si alguno es 0 "Error"
	elif (num1 == 0) or (num2 == 0) :
		print("Error")
	#si el 1er es mayor ''Arriba'', si el 2do "Abajo"
	elif num1 > num2 :
		print("Arriba")
	else:
		print("Abajo")
	print("---------------------")
	if input("Desea continuar? si/no:\t") == "no":
		break
print("fin.")