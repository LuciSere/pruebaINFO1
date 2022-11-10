#DADO EL MONTO DE COMPRA DE UN CLIENTE
#si LA COMPRA es MAYOR A #10000 (diezmil)DESCONTAR 5%
#si la compra es mayor a 15000 (quincemil)descontar 10%
#si la compra es mayor a 50000 (cincuentamil)descontar un 20%
#si la compra es mayor a 100000 (cienmil)descontar un 30%
# MOSTRAR AL FINAL EL MONTO TOTAL Y EL DESCUENTO REALIZADO

monto = float(input("Ingrese el monto total de la compra: $"))
descuento = 0.00
porciento ="0%"

if (10000 < monto <= 15000):
	descuento = monto * 0.05
	porciento ="5%"
elif (15000 < monto <=50000):
	descuento = monto * 0.1
	porciento ="10%"
elif (50000 < monto <= 100000):
	descuento = monto * 0.2
	porciento ="20%"
elif (monto > 100000):
	descuento = monto * 0.3
	porciento ="30%"

monto = monto - descuento
print(f"El monto total a pagar es de: ${monto}, se le desconto un {porciento} que equivale a ${descuento}")
