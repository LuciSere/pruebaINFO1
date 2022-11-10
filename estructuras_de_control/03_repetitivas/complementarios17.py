'''
17) Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades 
si este se le asigna como un porcentaje de su salario mensual que depende de su 
antigüedad en la empresa de acuerdo con la sig. tabla:

Tiempo												Utilidad

Menos de 1 año								5% del salario

Más de 1 año y hasta 2 años				  	 7% del salario

Más de 2 años y hasta 5 años				 10% del salario

Más de 10 años								 20% del salario
'''
while(True):
	#ingrese su sueldo y  antiguedad del trabajador
	sueldo = float(input("Ingese el sueldo mensual:\t$"))
	print("Seleccione segun la antiguedad del trabajador en la empresa:")
	print("1- Menos de 1 año\n2- Más de 1 año y hasta 2 años\n3- Más de 2 años y hasta 5 años\n4- Más de 10 años")
	antiguedad = int(input())
	while (antiguedad) < 1 or (antiguedad > 4):
		antiguedad =int(input("Opcion no valida.Seleccione la opcion correspondiente:\t"))

	if antiguedad == 1:
		utilidad = sueldo * 0.05
		porciento = "5%"
	elif antiguedad == 2:
		utilidad = sueldo * 0.07
		porciento = "7%"
	elif antiguedad == 3:
		utilidad = sueldo * 0.10
		porciento = "10%"
	elif antiguedad == 4:
		utilidad = sueldo * 0.20
		porciento = "20%"
	else:
		print("Opcion incorrecta")
		break
		
	print(f"Su salario es ${sueldo}\nPor su antiguedad recibe un {porciento} de utilidad: ${round(utilidad,2)}.\nEl monto total es: ${round(sueldo + utilidad,2)}")
	print("--------------------------------")
	if input("Desea continuar? si/no:\t") == "no":
		break
print("fin")