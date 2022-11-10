'''
vehiculo:color, ruedas
coche: velocidad(km/h), cilindrada(cc)
'''
#importo las clases que voy a usar
from clasesStone import Vehiculo, Coche

## Programita
auto = Coche('Rojo', 4, 120, 300)
auto.setCilindrada(400)
moto = Vehiculo('Azul',2)

print(f"{auto}\n{moto}")

