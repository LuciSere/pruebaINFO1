'''
Ejercicio 1: Triángulos
Escriba una función que tome las longitudes de los dos lados más cortos de un 
triángulo rectángulo como sus parámetros y devuelva la hipotenusa del triángulo, 
calculada usando el teorema de Pitágoras, como resultado de la función. Incluya 
un programa principal que lea las longitudes de los lados más cortos de un 
triángulo rectángulo del usuario, use su función para calcular la longitud de la 
hipotenusa y muestre el resultado.
'''

def hipotenusa(a,b):
	x = a ** 2 + b ** 2 #calculo la suma de los cuadrados de los lados mas cortos
	hipo = x ** 0.5 #aca saco la raiz cuadrada (investigar funcion pow y sqrt)