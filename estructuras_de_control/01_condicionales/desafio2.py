
print("\n Seleccione el tamañodel pez: \n")
print("1: Tamaño Normal")
print("2: Tamaño por debajo de lo Normal")
print("3: Tamaño un poco por encima de lo Normal")
print("4: Tamaño sobredimensionado\n")
opcion = input("digite el numero de la opción correspondiente: ")

if opcion == "1":
	print("Pez en buenas condiciones")
elif opcion == "2":
	print("Pez con problemas de nutrición")
elif opcion == "3":
	print("Pez con síntomas de organismo contaminado")
elif opcion == "4":
	print("Pez contaminado")
else:
	print("La opción ingresada es incorrecta.")


