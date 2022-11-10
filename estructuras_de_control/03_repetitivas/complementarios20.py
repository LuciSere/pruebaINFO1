'''
20) El Centro de Salud de Rosario tiene registradas N consultas médicas de menores. 
De cada consulta tiene como datos: la edad del menor y el día de visita. 
Los datos están ordenados en forma creciente por día. 
Proponer un fin de datos para cada día. 
Se desea conocer, para cada día, la edad promedio de pacientes 
y además el día en que se registró el máximo de pacientes.
'''
dia = 1
maximo = 0
# un while para cada dia
while True:
	contador_pacientes = 0
	suma_edad = 0
	if input(f"¿Hubo consulta el dia{dia}? si/no:\t") == "si":
		consulta = True
		#while para cada consulta del mismo dia.
		while consulta: 
			edad = int(input("Ingrese la edad del paciente: "))
			suma_edad += edad
			contador_pacientes += 1
			if input("Desea cargar otra consulta? si/no: \t") == "no":
				consulta = False
		print(f"El promedio de edad para el dis{dia} es: {suma_edad/contador_pacientes}")
	#guardo el dia que se regitro mas pacientes
	if contador_pacientes > maximo:
		maximo = contador_pacientes
		dia_maximo = dia
	dia += 1
	print("----------------------------")
	if input("Desea cargar el proximo dia? si/no:\t")=="no":
		break
#informo
print(f" El dia {dia_maximo} se registro la mayor cantidad de consultas, con un numero de: {maximo}")
print("fin")

