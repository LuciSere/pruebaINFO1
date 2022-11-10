'''
7) Realizar un programa que calcule y muestre la suma de los múltiplos de 5 
comprendidos entre dos valores A y B. 
El programa no permitirá introducir valores negativos para A y B 
y verificará que A es menor que B. 
Si A es mayor que B, se deben intercambiar los valores.


'''
#ingresar el rango.El programa no permitirá introducir valores negativos para A y B 
a = -1
b = -1
while a < 0 or b < 0:
	a = int(input("Ingrese un numero positivo para a:\t"))
	b = int(input("Ingrese un numero positivo para b:\t"))
#ordenar.verificará que A es menor que B. Si A es mayor que B, se deben intercambiar los valores.
if a > b :
	mayor = a
	menor = b
else:
	mayor = b
	menor = a
#es multiplo de 5? calcular la suma de los multiplos
suma_multiplos_5 = 0
for numero in range(menor,mayor,1):
	if numero % 5 == 0:
		suma_multiplos_5 += numero
#		print(f"\t {numero} es multiplo de 5")
#mostrar la suma de los multiplos
print(f"La suma de los multiplos de 5 comprendidos entre {a} y {b} es: {suma_multiplos_5}")