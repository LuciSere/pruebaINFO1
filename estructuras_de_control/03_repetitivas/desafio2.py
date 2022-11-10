desafio2.py
"""
Desafío 2
Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.

Realizá un programa que permita registrar cantidad de colillas recolectadas por un 
número determinado de personas. 
Luego obtener estadísticas al respecto informando porcentaje de personas que han 
encontrado menos de 100 colillas, más de 100 y menos de 200, más de 200 colillas.

"""
cantidadRecolectores = int(input("ingrese el numero de personas recolectoras:"))
contador = 0

menosDe100 = 0
menosDe200 = 0
masDe200 = 0

whil
'''
#programa del profe:

personas =int(input("ingrese la cantidad de personas"))
menos_100 = 0
menos_200 = 0
mas_200 = 0
for p in range(1,personas+1):
	cuantas = int(input(f"ingrese la cantidad de colillas recolectadas por la persona {p}"))
	if (cuantas > 200):
		mas_200 += 1
	elif (cuantas > 100):
		mas_100 += 1
	else:
		menos_100 += 1
por1 = (menos_100 * 100) / personas
por2 = (mas_100 * 100) / personas
por3 = (mas_200 * 100) / personas

print(f"La porcentaje de personas que han encontrado menos de 100 colillas es de {round(por1, 2)}%")

print(f"La porcentaje de personas que han encontrado mas de 100 colillas y menos de 200 es de {round(por2,2)}%")

print(f"La porcentaje de personas que han encontrado mas de 200 colillas es de {round(por3,2)}%")

//programa de renzo
print("Bienvendos a mi programa")

print("--------------------------")

acumulador1 = 0
por1 = 0
acumulador2 = 0
por2 = 0
acumulador3 = 0
por3 = 0
num = 0
des = ""
contador_persona = 0
bandera = True

print("Campaña de recolección de cigarrillos")
while (bandera):	
	num = int(input("Ingrese la cantidad de colillas que encontró esta persona\t")) 
	contador_persona = contador_persona + 1
	if(num <= 100):
		acumulador1 = acumulador1 + 1
	elif (num > 100 and num <=200):
		acumulador2 = acumulador2 + 1
	else:
		acumulador3 = acumulador3 + 1


	print("Desea continuar contando? 1- Si 2 - No")
	des = input("\t")
	if (des == "2"):
		bandera = False

por1 = (acumulador1 * 100) / contador_persona
por2 = (acumulador2 * 100) / contador_persona
por3 = (acumulador3 * 100) / contador_persona

print(f"La cantidad de personas que han encontrado menos de 100 colillas es de {round(por1, 2)}%")

print(f"La cantidad de personas que han encontrado mas de 100 colillas y menos de 200 es de {round(por2,2)}%")

print(f"La cantidad de personas que han encontrado mas de 200 colillas es de {round(por3,2)}%")
'''