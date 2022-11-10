'''
Ejercicio 2: Tarifa del taxi
En una jurisdicción particular, las tarifas de taxi consisten en una tarifa base 
de $40.00, más $15.00 por cada 140 metros recorridos. Escriba una función que 
tome la distancia recorrida (en kilómetros) como su único parámetro y devuelva 
la tarifa total como su único resultado. Escriba un programa principal que use 
la función.
Sugerencia: Utilice constantes para presentar la base y la porción variable de 
las tarifas así el programa podrá actualizar fácilmente cuando las tasas aumentan.
'''
def calcular_tarifa(km):
	BASE = 40.00
	METROS= km*1000
	PLUS = (metros/140) * 15.00
	if metros < 140:
		tarifa = base
	else:
		tarifa = base + plus
	return round(tarifa,2)

#------mi programa------

km = float(input("Ingrese los kilometros reccoridos:\t"))
resultado = calcular_tarifa(km)
print(f"La tarifa sera: ${resultado}.")