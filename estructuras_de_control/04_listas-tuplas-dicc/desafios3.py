'''
Desafío 3		
Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el 
email (no es necesario validar). Tendrás que ir pidiendo contactos hasta el 
usuario diga que no quiere insertar mas. No se podrán insertar nombres repetidos.

'''
diccionario = {}

while True:
	clave= input("Ingrese nombre del biologo:\t")
	valor = input("Ingrese email:\t")

	if clave in diccionario:	
		print(f"El diretorio {clave} ya fue guardado, no se puede remplazar")
	else:
		diccionario[clave]= valor

	if input("Desea agregar otro directorio? (s/n):\t") == "n":
		break
	
print(diccionario)
print("Fin del programa")