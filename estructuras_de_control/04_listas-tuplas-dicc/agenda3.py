


'''
Hacer una agenda, agregando personas a la agenda usando listas, hay que agregar nombre y teléfono.
'''


lista_nombres = []
lista_telefono = []

continuar = 's'

while (continuar == 's' or continuar == 'S'):
    print("---Menu de Agenda---")
    opcion = int(input("Por favor, seleccione una opcion\n(1-Agregar un contacto, 2-Modificar un contacto, 3-Mostrar un contacto): "))

    if (opcion == 1):
        print("---Agregar un contacto---")
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el numero de telefono: ")
        lista_nombres.append(nombre)
        lista_telefono.append(telefono)

        continuar = input("--Presione s para volver al menu, cualquier otra tecla para finalizar--")
    elif(opcion == 2):
        cambiar = int(input("En proceso"))

    else:
        contacto = int(input("Ingrese el indice del contacto al que quiere acceder: "))
        print("---CONTACTO---")
        print(lista_nombres[contacto])
        print(lista_telefono[contacto])
        print("--------------")


print(lista_nombres)
print(lista_telefono)
