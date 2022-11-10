'''Realizar una agenda, que se pueda guardar nombre y teléfono.'''
from turtle import pos


listPerson= []
listPersonPhone= []
flag= False
position=0
def savePerson(name): #alex #fulanito
    listPerson.append(name) #0 #1

def PersonPhone(phone):
    listPersonPhone.append(phone)

def reset(position, flag):
    position=0
    flag= False

follow= 'SI'
while(follow == 'SI'):
    decision= input("¿Que desea realizar?\n1.Agregar un contacto\n2.Buscar un contacto.\nRespuesta: ")
    if decision == '1':
        name= input("Ingrese por favor su nombre: ")
        phone= int(input("Ingrese por favor su numero de telefono: "))
        savePerson(name.upper())
        PersonPhone(phone)
        print("Contacto agregado!")
    elif decision == '2':
        if listPerson != []: #if len(listPerson) == 0 #if bool(listPerson)
            decision= input("¿Como desea buscarlo?\n1.Por su nombre.\n2.Por su numero de telefono\nRespuesta: ")
            if decision == '1':
                name= input("Ingrese por favor el nombre de la persona: ")
                name= name.upper()
                for i in listPerson: #i= alex #i=fulanito in listPerson(5)
                    if name == i:
                        print(f"Contacto encontrado:\nNombre: {listPerson[i]}.\nNumero de telefono: {listPersonPhone[position]}")
                        flag= True
                    position+=1

                if flag != True:
                    print("El contacto no se encontro.")
                reset(position, flag)

            if decision == '2':
                phone = int(input("Ingrese por favor el numero de telefono de la persona: "))
                for i in listPersonPhone: #213131 #12312313 
                    if phone == i:
                        print(f"Contacto encontrado: Nombre: {listPerson[position]}.\nNumero de telefono: {listPersonPhone[i]}")
                        flag = True
                    position+=1

                if flag != True:
                    print("El usuario no se encontro.")
                reset(position, flag)
    else:
        print("Usted no ingreso una opcion correcta.")
        follow= input("¿Desea seguir agregando/buscando?..\nGuia\t'SI' para continuar.\n\tCualquier tecla para salir.\nRespuesta: ")
        follow= follow.upper()
                


                






