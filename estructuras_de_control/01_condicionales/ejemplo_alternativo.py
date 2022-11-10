#DADO EL MONTO DE COMPRA DE UN CLIENTE, OFRECER UN DESCUENTO DEL 10%
#SIEMPRE Y CUANDO LA COMPRA SEA MAYOR A #10000
#PERO SI LA MISMA ES MENOR O IGUAL A 10000, INCREMENTARLE UN 5%

monto = float(input("Ingrese el monto total de la compra: $"))

if (monto > 10000):
	decuento = monto * 0.1
	monto = monto - descuento #se hace el 10%d e descuento
	print(f"El monto total a pagar es de: ${monto}, de le desconto un 10% que evivale a ${descuento}")
else:
	aumento = monto * 0.05
	monto = monto + aumento #se hace el 05% de incremento
	print(f"El monto total a pagar es de: ${monto}, de le aumento un 5% que evivale a ${aumento}")

