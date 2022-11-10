
def primo(number):
    if number < 2:
        return False

    for n in range(2, number):
        if number % n == 0:
            return False

    return True

if __name__  == '__main__': #esto le dice a python que solo ejecute esto si se llama al archivo funciones.py, 
	print('Hola')#			 es decir si importe alguna funcion  en otro archivo esto no se va ejecutar.
