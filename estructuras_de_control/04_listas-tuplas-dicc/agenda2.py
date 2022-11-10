#Hacer una agenda, agregando personas a la agenda usando listas, 
#hay que agregar nombre y teléfono


nombres = []
numeros = []


print("----------Bienvenido a tu agenda----------")


continuar = "si"

while continuar.lower() == "si":
    print("MENU")
    print("1 - Ingrese un nuevo contacto")
    print("2 - Ver contactos")
    opcion = int(input("Ingrese opción: "))
    if opcion == 1:
        n1 = input("Ingrese el nombre del contacto: ")
        nombres.append(n1)
        n2 = int(input("Ingrese el número del contacto: "))
        numeros.append(n2)
    if opcion == 2:
        print(nombres)
        print(numeros)
    continuar = input("¿Desea realizar otra operación? ")

print()
print("Gracias por ver tu agenda.")