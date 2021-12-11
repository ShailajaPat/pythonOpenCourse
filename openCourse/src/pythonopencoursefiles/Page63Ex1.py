class Person(object):
     species = "Homo sapiens"
     def talk(self):
          return "Hello there, how are you?"

somebody = Person()
somebody.species = 'Homo internetus'
somebody.name = 'Mark'
nobody = Person()
print(nobody.species)
print(somebody.species)
Person.name = 'Unknown'
print(nobody.name)
print(somebody.name)
del somebody.name
print(somebody.name)
