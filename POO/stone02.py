'''
https://sites.google.com/view/informatorio-poo/level-stone?authuser=0

Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos.

Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra
 mostrando el nombre de su clase y sus atributos.

Modifica la función catalogar() para que reciba un argumento optativo ruedas, 
haciendo que muestre únicamente los que su número de ruedas concuerde con el valor 
del argumento. También debe mostrar un mensaje "Se han encontrado {} vehículos con {}
 ruedas:" únicamente si se envía el argumento ruedas. 
 Ponla a prueba con 0, 2 y 4 ruedas como valor.

'''
###  Clases Objetos
from clasesStone import *

###  Funciones
from funcionesStone import catalogar

###  programa
vehi = Vehiculo("Rojo", 4)
auto = Coche("Negro", 4, 120, 300)
bici = Bicicleta("Blanca", 2, "Deportiva")
moto = Motocicleta("Gris", 2, "Urbana", 60, 150)
cami = Camioneta("Verde", 4, 180, 400, 500)
#print(f"{vehi}\n{auto}\n{bici}\n{moto}\n{cami}")

vehiculos = [vehi,auto,bici,moto,cami]
print("------------------------------------")
catalogar(vehiculos)
print("------------------------------------")
catalogar(vehiculos, 0)
print("------------------------------------")
catalogar(vehiculos, 2)
print("------------------------------------")
catalogar(vehiculos, 4)
print("------------------------------------")
catalogar(vehiculos, 3)

