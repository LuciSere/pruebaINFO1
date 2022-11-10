'''
Hacer una agenda - Usar solo listas para guardar nombre y telefono.
Agregar personas a la agenda y mostrarlas.
'''
def agregar(lista_1: list) -> list:
    nombre = input("Ingrese nombre contacto: ")
    telefono = input("Ingrese telefono contacto: ")
    lista_x = [nombre, telefono]
    lista_1.append(lista_x)
    return lista_1

def buscar(lista_1):
    lista_respuesta = list()
    nombre = input("Ingrese nombre para buscar: ")
    for elemento in lista_1:
        if nombre == elemento[0]:
            lista_respuesta.extend(elemento)

    if len(lista_respuesta) == 0:
        return lista_respuesta, False
    return lista_respuesta, True


lista_1 = list()
while(True):
    print("Seleccione 1 para agregar contacto. ")
    print("Seleccione 2 para buscar contacto. ")
    print("Seleccione 3 para salir")
    seleccion = int(input("\t"))

    if seleccion == 1:
        lista_1 = agregar(lista_1)
    
    if seleccion == 2:
        lista_aux, booleano = buscar(lista_1)
        if booleano:
            print(lista_aux)
        else:
            print("Contacto no encontrado")

    if seleccion == 3:
        print("Saliendo del programa")
        break

print(f"Lista: {lista_1}")
    

