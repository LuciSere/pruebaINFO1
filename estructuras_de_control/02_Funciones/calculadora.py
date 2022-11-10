'''
Ejercicio, calculadora (con iterador y funciones)
Ingrese 2 valores;
Pregunar si quiere sumar, restar, multiplicar, dividir.;
Preguntar denuevo hasta q decida salir;
'''
def suma(a,b):
	return a + b
def resta(a,b):
	return  a - b
def multi(a,b):
	return  a * b
def divi(a,b):
	if b != 0:
		return  a / b
	else:
		return "Error. Division por 0 es invalida."

while True:
	a = float(input("Ingrese un numero:\t"))
	b = float(input("Ingrese otro numero:\t"))

	print("¿Que operacion desea realizar?:")
	print(" 1: Suma\n 2: Resta\n 3: Multiplicación\n 4: División\n")
	opcion = int(input("ingrese:\t"))
	if opcion == 1:
		print(f"El resultado es: \n\t{a} + {b} = {suma(a,b)}\n")
	elif opcion == 2:
		print(f"El resultado es: \n\t{a} - {b} = {resta(a,b)}\n")
	elif opcion == 3:
		print(f"El resultado es: \n\t{a} * {b} = {multi(a,b)}\n")
	elif opcion == 4:
		print(f"El resultado es: \n\t{a} / {b} = {divi(a,b)}\n")
	else:
		print("Opcion incorrecta\n")
	print("----------------------------")
	if input("¿Desea continuar? s/n:\t") == "n":
		break
print("\nGracias por utilizar mi programa.\n")