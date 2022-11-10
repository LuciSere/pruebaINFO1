'''
Ejercicio 6: Centrar una cadena en la terminal
Escriba una función que tome una cadena de caracteres como primer parámetro y el 
ancho de la terminal en caracteres como segundo parámetro. Su función debe 
devolver una nueva cadena que consta de la cadena original y el número correcto 
de espacios iniciales para que la cadena original aparezca centrada dentro del 
ancho proporcionado cuando se imprima. No agregue ningún carácter al final de la 
cadena. Incluya un programa principal que use su función.
'''

def centrar_cadena(cadena,ancho_terminal):
	espaciosN = (ancho_terminal - len(cadena)) // 2 #numero de espacios tipo int
	espaciosC= " " * espaciosN #cadena de espacios. tipo string
	imprimir = espaciosC + cadena
	return imprimir

#programa

ancho_terminal = 117
cadena = input("ingrese una cadena:\t")
nueva_cadena = centrar_cadena(cadena,ancho_terminal)
print(nueva_cadena)


