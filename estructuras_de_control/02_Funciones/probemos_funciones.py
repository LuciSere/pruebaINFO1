

# -*- coding: utf8 -*-

"""Funciones en Python		contine las funciones:
								iva()
								suma(numero1,numero2)
								imprime_fibonacci(n)
								devuelve_fibonacci(n)
"""

def iva():
    '''función básica para el calculo del IVA'''
    iva = 12
    costo = float(input('¿Cual es el monto a calcular?: '))
    calculo = costo * iva / 100
    print (f"El calculo de IVA es: {str(calculo)}\n")


def suma(numero1,numero2):
    '''función la cual suma dos números'''
    print (numero1 + numero2)
    print ("\n")


def imprime_fibonacci(n):
    '''escribe la sucesión Fibonacci hasta n. Un numero por linea. (return = None)'''
    a, b = 0, 1
    while b < n:
        print (b),
        a, b = b, a + b


def devuelve_fibonacci(n): 
    '''devuelve la sucesión Fibonacci hasta n. Como una lista'''
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a + b
    return resultado

#Programa

mensaje = "Calcular el IVA de un monto"
print (mensaje)
print ("=" * len(mensaje) + "\n")
iva()

mensaje1 = "Suma de dos números"
print (mensaje1)
print ("=" * len(mensaje1) + "\n")
print("13 + 37 =")#yo agregue esta linea
suma(13,37)


mensaje2 = "Sucesión de Fibonacci"
print (mensaje2)
print ("=" * len(mensaje2) + "\n")

print ("La sucesión Fibonacci hasta 10 es:", imprime_fibonacci(10))

print ("\nLa sucesión Fibonacci hasta 50 es:", devuelve_fibonacci(50))