'''
Ejercicio 18: Días en un mes
Escriba una función que determine mostrar cuántos días hay en un mes en 
particular. Su función tomará dos parámetros: el mes como un número entero entre 
1 y 12, y el año como un número entero de cuatro dígitos. Asegúrese de que su 
función informa el número correcto de días en febrero para los años bisiestos. 
Incluya un programa principal que lea un mes y un año del usuario y muestre el 
número de días en ese mes.

cuantos dias hay en un mes especifico?
funcion toma 2 parametros
mes como entero
año numero entero de 4 digits
tener encuenta los dias de febrero para un año bisiesto
Meses con 30 días: Abril4, Junio6, Septiembre9 y Noviembre11.
Meses con 31 días: Enero 1, Marzo3, Mayo5, Julio7, Agosto8, Octubre10 y Diciembre12.
Meses con 28 días: Febrero 2 (Menos cuando es bisiesto que tiene 29 días).

'''
def anio_bisiesto(anio):
	bisiesto = False
	if anio > 1582:
		if (anio % 100 == 0) and (anio % 400 == 0):
			bisiesto = True
		elif(anio % 100 != 0) and (anio % 4 == 0):
			bisiesto = True
	return bisiesto


def dias_mes(mes, anio):
	dias = "Fuera de rango"
	if (anio == 1582) and (mes == 10):
		dias = 21	
	elif (mes == 4) or (mes ==6) or (mes ==9) or (mes ==11):
		dias = 30
	elif (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
		dias = 31
	elif mes == 2:
		if anio_bisiesto(anio):
			dias = 29
		else:
			dias = 28
	return dias

# programa

print("Este programa le dira la cantidad de dias del mes y año proporcionado por el usuario")
anio = int(input("Ingrese un año (AAAA):\t"))
mes = int(input("Ingrese el numero de mes:\t"))

if(anio < 1000) or (anio > 9999):
	print("Error: año fuera de rango.")
elif(mes < 1) or (mes > 12):
	print("Error: mes fuera de rango.")
else:
	print(f"En el año {anio} el mes {mes} tiene {dias_mes(mes, anio)} dias.")


