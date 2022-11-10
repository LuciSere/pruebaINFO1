'''
#que hace este progra?

letra=input("Letra:")
if len(letra)!=1:
    print("Debe ser sólo una letra")
else:
    if letra in "aeiou":
        print("Es vocal")

#se colocan los operadores que corresponde

a=5
b=6
c=4
if (a>b and a>c):
    print ("a es mayor que b y que c")
elif (a > b and a<c):
    print ("a es mayor que b pero no es mayor que c")
elif (a<b and a > c):
    print ("a es mayor que c pero no es mayor que b")
else:
    print ("a no es mayor que b ni mayor que c")   



#Suponiendo que estamos realizando un programa en python que simule arrojar 
#tres dados, en informe al usuario si al menos alguno de los dados obtuvo el 
#valor de 6, complete con el operador que corresponda.   

import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)
if dado1 == 6 or dado2 == 6 or dado3 == 6:
    print("Victoria!")

# debe imprimir 5 veces 
contador = 1
while contador <= 5 :
    print("Hola, mundo")
    contador = contador + 1    
'''


