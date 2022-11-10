'''
Crear una clase Tiempo, con atributos hora, minuto y segundo, 
que pueda ser instanciada indicando: los tres atributos, sólo la hora y minuto,
o sólo la hora. Crear además los métodos necesarios 
para modificar la hora en cualquier momento de forma manual. 
Mantenga la integridad de los datos en todo momento definiendo de tipo “private”. 
Crear  una  clase prueba_tiempo que  prueba  una  hora  concreta  y  
la  modifique  a  su  gusto  mostrándola  por pantalla.
'''
class Tiempo(hs, min=00, sec=00):
	def __init__(self):
		self.hora = hs
		self.minuto = min
		self.segundo = sec

	def __str__(self):
		return f"La hora actual es: {self.hora} horas, {self.minuto} minutos y {self.segundo} segundos"

	def setHora(self, hs_nueva):
		self.hora = hs_nueva

	def setMinuto(self, min_nuevo):
		self.minuto = min_nuevo

	def setSegundo(self, sec_nuevo):
		self.segundo = sec_nuevo

class Prueba_tiempo:
