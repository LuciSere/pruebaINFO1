
#solucion en Programacion Estructurada
'''
# Definimos unos cuantos clientes
clientes= [
    {'Nombre': 'Hector', 'Apellidos':'Costa Guzman', 'dni':'11111111A'},
    {'Nombre': 'Juan', 'Apellidos':'González Márquez', 'dni':'22222222B'} 
]

# Creamos una función que muestra un cliente en una lista a partir del DNI
def mostrar_cliente(clientes, dni):
    for c in clientes:
        if (dni == c['dni']):
            print('{} {}'.format(c['Nombre'],c['Apellidos']))
            return
    print('Cliente no encontrado')

# Creamos una función que borra un cliente en una lista a partir del DNI
def borrar_cliente(clientes, dni):
    for i,c in enumerate(clientes):
        if (dni == c['dni']):
            del( clientes[i] )
            print(str(c),"> BORRADO")
            return

    print('Cliente no encontrado')    

### Observa muy bien cómo se utiliza el código estructurado

print("==LISTADO DE CLIENTES==")
print(clientes)

print("\n==MOSTRAR CLIENTES POR DNI==")
mostrar_cliente(clientes, '11111111A')
mostrar_cliente(clientes, '11111111Z')

print("\n==BORRAR CLIENTES POR DNI==")
borrar_cliente(clientes, '22222222V')
borrar_cliente(clientes, '22222222B')

print("\n==LISTADO DE CLIENTES==")
print(clientes)
'''

#Solucion en POO

# Creo una estructura para los clientes
class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)

# Y otra para las empresas
class Empresa:

    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")

    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO")
                return
        print("Cliente no encontrado")

### Ahora utilizaremos ambas estructuras 

# Creemos un par de clientes
hector = Cliente(nombre="Hector", apellidos="Costa Guzman", dni="11111111A")
juan = Cliente("22222222B", "Juan", "Gonzalez Marquez")

# Creemos una empresa con los clientes iniciales
empresa = Empresa(clientes=[hector, juan])

# Se muestran todos los clientes
print("==LISTADO DE CLIENTES==")
print(empresa.clientes)

print("\n==MOSTRAR CLIENTES POR DNI==")
# Se consulta clientes por DNI
empresa.mostrar_cliente("11111111A")
empresa.mostrar_cliente("11111111Z")

print("\n==BORRAR CLIENTES POR DNI==")
# Se borra un cliente por DNI
empresa.borrar_cliente("22222222V")
empresa.borrar_cliente("22222222B")

# Se muestran de nuevo todos los clientes
print("\n==LISTADO DE CLIENTES==")
print(empresa.clientes)
