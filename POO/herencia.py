
#Alumno: DNI, NOMBRE, SEXO, LEGAJO, CARRERA

#Profesor: DNI, NOMBRE, SEXO, LEGAJO, ANTIGUEDAD

class Persona:
	def __init__(self, dni,nombre, sexo, legajo):
	self.dni = dni
	self.nombre = nombre
	self.sexo = sexo
	self.legajo = legajo

	def getNombre(self):
		return self.nombre 
	def setNombre(self, nuevo_nombre)
		self.nombre = nuevo_nombre

	def __str__(self):
		return f"Persona: {self.nombre}, DNI: {self.dni}"
#p = Persona(333333,'nicolas','M',17888)
#x = Persona(444444,'Camila','F',55555)

class Alumno(Persona):
	def __init__(self, dni,nombre, sexo, legajo, carrera):
		super(). __init__(dni,nombre, sexo, legajo)
		self.carrera = carrera

	def __str__(self):
		return f"Alumno: {self.nombre}, DNI: {self.dni}"

class Profesor(Persona):
	def __init__(self, dni,nombre, sexo, legajo, antiguedad):
		super(). __init__(dni,nombre, sexo, legajo)
		self.antiguedad = antiguedad

	def __str__(self):
		return f"Profesor: {self.nombre}, DNI: {self.dni}"

a = Alumno(30000000,'Nicolas','M' ,17888,'ISI')
p = Profesor(38000000,'Maria','F' ,19888, 10)