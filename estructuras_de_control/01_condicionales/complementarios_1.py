complementarios_1.py

numero1 = int(input("Ingrese el 1er numero: "))
numero2 = int(input("Ingrese el 2do numero: "))
numero3 = int(input("Ingrese el 3ro numero: "))

print("Los numeros ordenados de menos a mayor son: ")
#menor=min(numero1,numero2,numero3)
#mayor=max(numero1,numero2,numero3)
#medio=(numero1+numro2+numero3)-(menor+mayor)

if numero1<numero2 and numero1<numero3:
	if numero2<numero3:
		print(numero1,numero2,numero3)
	else:
		print(numero1,numero3,numero2)
elif numero2<numero1 and numero2<numero3:
	if numero1<numero3:
		print(numero2,numero1,numero3)
	else:
		print(numero2,numero3,numero1)
elif numero3<numero1 and numero3<numero2:
	if numero1<numero2:
		print(numero3,numero1,numero2)
	else:
		print(numero3,numero2,numero3)
else
	if numero1 == numero2 
		print(numero3,numero1,numero2)
	elif numero3 == numero2:
		print(numero3,numero2,numero1)
	else:
		print(numero1,numero2,numero3)