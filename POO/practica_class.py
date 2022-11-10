class Profesor:
	def __init__(self, nombre, materia, aula="Zoom"):
		self.nombre = nombre
		self.materia = materia
		self.aula = aula

	def mostrar_nombre(self):
		print(f"Mi nombre es: {self.nombre}")

	def mostrar_materia(self):
		print(f"Enseño la materia: {self.materia}")

	def mostrar_aula(self):
		print(f"Mis clases se dictan en el aula: {self.aula}")

	def modificar_aula(self,nueva):
		self.aula = nueva

	def calificar(self, alumno, nota):
		alumno.agregar_nota(nota)


class Estudiante:
	def __init__(self, nombre, materia):
		self.nombre = nombre
		self.materia = materia
		self.nota = [5, 5]
		self.promedio_general = sum(self.nota) / len(self.nota)

	def mostrar_nombre(self):
		print(f"Mi nombre es: {self.nombre}")

	def mostrar_materia(self):
		print(f"Estudio la materia: {self.materia}")

	def mostrar_nota(self):
		print(f"Mis calificaciones: {self.nota}")

	def agregar_nota(self,nueva):
		self.nota.append(nueva)

	def mostrar_promedio(self):
		print(f"Mi promedio general es: {self.promedio_general}")

##Fuera

alumno1 = Estudiante("Ludmila","Programacion")
alumno1.mostrar_nombre()
alumno1.mostrar_materia()
print("")

alumno2 = Estudiante("Martin","Ingenieria")
alumno2.mostrar_nombre()
alumno2.mostrar_materia()
print("")
profe1 = Profesor("Nicolas","Programacion")
profe1.mostrar_nombre()
profe1.mostrar_materia()
profe1.mostrar_aula()
print("")
profe1.calificar(alumno1, 8)
alumno1.mostrar_nombre()
alumno1.mostrar_nota()
alumno1.mostrar_promedio()
print("")
profe1.calificar(alumno2, 7)
alumno2.mostrar_nombre()
alumno2.mostrar_nota()
alumno2.mostrar_promedio()


