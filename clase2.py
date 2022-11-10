'''
#creo una variable que se llama nombre, y guardo "NICOLAS TORTOSA"
nombre = "NICOLAS TORTOSA" #String = Cadena
edad = 33 #int --> Integer --> Entero

########################################################################

precio = 100
precio_con_iva = precio * 1.21
print("La variable nombre contiene un/a", type(nombre))#string
print("La variable edad contiene un/a", type(edad))#int
print("La variable precio contiene un/a", type(precio))#int
print("La variable precio_con_iva contiene un/a", type(precio_con_iva))#float
'''
########################################################################
'''
#TODO LO QUE INGRESO POR TECLADO(INPUT) VA A SER STRING
x = 33 
y = "33"
print("la variable x contiene: ",type(x))
print("la variable y contiene: ",type(y))

edad1 = input("Ingrese su edad: ")
print("la variable edad1 contiene: ",type(edad1))
'''
########################################################################
'''
#a = 2
#b = "2"
#c = a + b
#print(c)	#TypeError: unsupported operand type(s) for +: 'int' and 'str'

num = 10
print(f"la variable num vale {num} es de tipo {type(num)}")
num2 = int(num) 
#int()      para pasar a entero
#float()    para pasar a numero flotante--> float
#str()      para pasar a string

#DOS MANERAS DISTINTAS DE MOSTRAR EL MISMO MJE
print(f"la variable num2 vale {num2} es de tipo {type(num2)}")# F DE FORMAT
print("la variable num2 vale", num2, "es de tipo", type(num2))# SIN FORMATO
'''
########################################################################



