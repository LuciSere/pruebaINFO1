'''
13) Un grupo de 100 estudiantes presentan un exámen de Física. Diseñe un diagrama 
que lea por cada estudiante la calificación obtenida y calcule e imprima:

A.- La cantidad de estudiantes que obtuvieron una calificación menor a 50.

B.- La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero 
menor que 70.

C.- La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero 
menor que 80.

D. La cantidad de estudiantes que obtuvieron una calificación de 80 o más.

'''
ra = 0
rb = 0
rc = 0
rd = 0

for est in range(1,6):#range(1,101)
	calificacion = int(input(f"Ingrese la calificacion del estudiante {est}:\t"))

	if calificacion < 50:
		ra += 1
	elif 50 <= calificacion < 70:
		rb += 1
	elif 70 <= calificacion < 80::
		rc += 1
	else: # calificacion>=80:
		rd += 1
print("---------RESULTADOS---------")
print(f"La cantidad de estudiantes con una calificacion menor a 50 es: {ra}")
print(f"La cantidad de estudiantes con una calificacion de 50  o mas, pero menor que 70: {rb}")
print(f"La cantidad de estudiantes con una calificacion de 70  o mas, pero menor que 80: {rc}")
print(f"La cantidad de estudiantes con una calificacion de 80 o mas es: {rd}")
