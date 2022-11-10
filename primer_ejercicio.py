 #El usuario compra tres productos 
 #- Ingresa la cantidad de cada producto que compro 
 #- calcular el monto total del usuario + iva

#pido precio y cantidad 1
precio1 = float(input("ingrese precio del producto 1: $"))
cantidad1 = int(input("ingrese cantidad de este producto: "))

#pido precio y cantidad 2
precio2 = float(input("ingrese precio del producto 2: $"))
cantidad2 = int(input("ingrese cantidad de este producto: "))

#pido precio y cantidad 3
precio3 = float(input("ingrese precio del producto 3: $"))
cantidad3 = int(input("ingrese cantidad de este producto: "))

#calculo el monto a pagar
compra = precio1 * cantidad1 + precio2 * cantidad2 + precio3 * cantidad3

#afrefo el iva a ese monto
compra_con_iva = compra * 1.21

#muestro el resultado
print("--------------------------------------------------")
print(f"el monto total del usuario es ${compra_con_iva}")

