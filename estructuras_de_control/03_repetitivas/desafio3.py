'''
Desafío 3
En una tienda de descuento por reciclado las personas que van a pagar 
el importe de su compra llegan a la caja y ofrecen tapitas para reciclar, 
de acuerdo a la cantidad que lleven en la caja le entregan un código de
 descuento que se aplicará sobre el total de su compra. Determinar la cantidad 
que pagara cada cliente desde que la tienda abre hasta que cierra. 

Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento;
 si es amarilla un 25% y si es blanca no obtendrá descuento.
 rojo = compra * 0.4
 amarilla = compra * 0.25
  blanca = 0

'''
descuento = 0
compra_con_descuento = 0

while(True):
	compra = float(input("ingrese el total de la compra: $"))
	codigo = (input("Ingrese el codigo correspondiente: \nrojo\namarilla\nblanca\n"))
	if codigo == "rojo":
		descuento = compra * 0.4
	elif codigo == "amarilla":
		descuento = compra * 0.25
	elif codigo == "blanca":
		descuento = 0
	else:
		print("el codigo es incorrecto")
	compra_con_descuento = round((compra - descuento),2)

	print("El total de la compra con el descuento aplicado es: ",compra_con_descuento)
	desicion = input("Desea continuar:\nsi \nno\t")
	if desicion == "no":
		break
print("Muchas gracias por su compra. Vuelva pronto")