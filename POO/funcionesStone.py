#funcion para el caso 2
def catalogar(lista,rueda = None):
	if rueda != None:
		cantidad = 0
		lista2 = []
		for i in lista:
			if i.getRuedas() == rueda:
				cantidad += 1
				lista2.append(i)
		if cantidad == 0:
				print(f"No se encontraron vehiculos con {rueda} ruedas.")
		else:	
			print(f"Se han encontrado {cantidad} vehículos con {rueda} ruedas:")
			for i in lista2:
				print("\t - " + i.__str__())	

	else:
		for i in lista:
			print(i.__str__())
			print(f"Es de la Clase: {type(i).__name__}\n")