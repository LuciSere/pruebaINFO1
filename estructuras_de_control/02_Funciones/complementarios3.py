'''Ejercicio 3: Calculadora de envío
Un minorista en línea proporciona una forma de envío urgente de $ 10.95 para el 
primer elemento y $ 2.95 para cada segundo elemento posterior. Escriba una 
función que tome el número de elementos en el pedido como su único parámetro. 
Devuelva los gastos de envío del pedido como resultado de la función. Incluya un 
programa principal que lea la cantidad de artículos comprados al usuario y 
muestre los gastos de envío.'''

#fuciones

def calcular_envio(cantidad):	
	if cantidad == 1:
		costo = 10.95
	else:
		costo = 10.95 + (cantidad//2) * 2.95# duda con la frace "cada segundo elemento posterior"
	return costo

#Programa
print("\nEste programa calcula el precio de ENVIO URGENTE segun la cantidad de elementos.")

cantidad = int(input("\nIngrese la cantidad de elementos a comprar: \t"))

if cantidad < 1:
	print("Error. La cantidad minima es: 1")
else:
	envio = calcular_envio(cantidad)
	print(f"El precio de envio por {cantidad} elemento/s es: ${envio}")
