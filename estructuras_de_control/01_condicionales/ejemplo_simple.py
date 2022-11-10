#dado el monto de compra de un cliente, ofrecer un descuento del 10%
#siempre y cuano la compra sea mayor a #10000 diezmil

monto = float(input("Ingrese el monto total de la compra: $"))

if (monto > 10000):
	monto = monto * 0.9 #se hace el 10%de descuento

print(f"El monto total a pagar es de: ${monto}")