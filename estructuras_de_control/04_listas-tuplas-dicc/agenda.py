
'''
hacer una agenda
solo usando listas
agregar personas a la agenda: nombre y telefono
quiere agregar o buscar un contacto?
mostrar


'''
def crear_cargar_lista():
	a = [] #yo pondria nombres mas descriptivos
	b = []
	print("Ingrese una lista de contactos, inserte 0 si desea terminar de cargar")#yo le pondria aparte la desicion de continuar cargando
	while True:
		nombre = input("Ingrese un nombre: \t")
		telefono = input("Ingrese el telefono: \t")
		if nombre == "0": 
			break
		else:
			a.append(nombre)# yo intentariaq agregar asi : nombre, telefono
			a.append(telefono)
			b.append(a)
			a = []
	return b

def recuperar_dato(lista, clave):
	tamanio = len(lista)
	i=0
	j=0
	while i != tamanio:
#	for i in range(tamanio):
		if nombre == lista[i][j]:
			print(lista[i])
		i +=1

# Programa
print("Este programa creauna agenda de contactos,con nombre y telefono, y te permite consultarla.")

lista = crear_cargar_lista()
print(f"Lista cargada:\n {lista} \n")

nombre = input("Ingrese el nombre del contacto que quiere mostrar:\t")
recuperar_dato(lista, nombre)



