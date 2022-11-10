print("examen POO 29/07/22\n")
'''
class test:
	def __init__(self):
		self.variable ="Old"
		self.Change(self.variable)

	def Change(self, var):
		var = "New"

obj = test()
print(obj.variable)'''
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
intanciar_dog = Dog("Rufus", 3)...

class Dog:
	species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
    	return f"{self.name} is {self.age} years old"

    def speak(self, sound):
    	return f"{self.name} says {sound}"'''
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Jrt(Dog):
	pass

class Dch(Dog):
	pass

class Bdog(Dog):
	pass

miles = Jrt("Miles",4)
buddy = Dch("Buddy",9)
jack = Bdog("Miles",4)
jim = Bdog("Miles",4)

print("a")
print(isinstance(miles, Dog))

print("b")
print(isinstance(jack, Dog))

print("c")
print(isinstance(miles, Bdog))

print("d")
print(isinstance(miles, Dog))

print("e")
print(isinstance(jack, Dch))'''

class Dog:
	species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
    	return f"{self.name} is {self.age} years old"

    def speak(self, sound):
    	return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

d1 = Dog("abvril",3)
print(d1.speak("wau"))

d2 = GoldenRetriever("abvril",3)


