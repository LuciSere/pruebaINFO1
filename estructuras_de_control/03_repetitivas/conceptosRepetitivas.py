conceptosRepetitivas.py
# FOR
N =10
N= int input("ingrese la cantidad")
for(i = 1 hasta N; i+1){
	i siempre es entero
]le


#iterables: cualquier estructura de datos que son iterables.

# nicolas
#(1,2,3,4,5,6) tupla
#[1,2,3,4,5,6] lista
#{clave: valor} diccionario
#objetos

#rango --> (valorInicial,valorFinal, incremento) --> range(1,10,1) el valor final, tengo que sumarle uno.
#POR DEFECTO EL VALOR INICIAL ES 0 Y EL INCREMENTO 1 range(10) mostraria del 0 al 9

for i in(1,2,3,4,5,6):
print("hola")

for i in [(1,2),[3,4,5],('a','b','c')]: #aqui hay 3 objetos, va iterar 3 veces.
print(i)

n = int(input("ingrese cuantos numeros quiere mostrar"))
for i in range(n+1):
	print(i)