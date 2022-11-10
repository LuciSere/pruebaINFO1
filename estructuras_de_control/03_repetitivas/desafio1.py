
""""
Desafío 1
Nos han pedido desarrollar una aplicación móvil
 para reducir comportamientos inadecuados para el ambiente.

a) Te toca escribir un programa que simule el proceso de 
Login. Para ello el programa debe preguntar al usuario 
la contraseña,
y no le permita continuar hasta que la haya ingresado 
correctamente.

b) Modificar el programa anterior para que solamente 
permita una cantidad fija de intentos. 

"""
# Creacion de usuario y contraseña
print("----------------------------------------\n")
print("Sing In / Registro del usuario\n")
usuario_guardado = input("Cree su nombre de usuario:\t")
contrasenia_guardada = input("Cree su contraseña:\t\t")

'''
# Login a: solo termina el ciclo cuando usuario y contraseña sean correctos.
print("----------------------------------------\n")
print("Log In / Ingreso\n")
bandera = True
while(bandera == True):
	usuario = input("Ingrese su nombre de usuario:\t")
	contrasenia = input("ingrese su contraseña:\t\t")
	if (usuario == usuario_guardado and contrasenia == contrasenia_guardada):
		print("Ud ingreso a sistema.")
		bandera = False
	else:
		print("Usuario o Contraseña incorrecta. Vuelva a intentar")
'''

# Login b: tiene una determinada cantidad de intentos(3)
print("----------------------------------------\n")
print("Log In / Ingreso\n")
contador = 1
while(contador <= 3):
	usuario = input("Ingrese su nombre de usuario:\t")
	contrasenia = input("ingrese su contraseña:\t\t")
	
	if (usuario == usuario_guardado and contrasenia == contrasenia_guardada):
		print("Felicitaciones.Ud ingreso a sistema.")
		break
	elif contador == 3:
		print("Ha sido bloqueado porque exedido los intentos permitidos. Intente mas tarde")
		break
	else:
		print("Usuario o Contraseña incorrecta. Vuelva a intentar")
		contador += 1
