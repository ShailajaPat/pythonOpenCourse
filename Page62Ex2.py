class Person(object):
     species = "Homo sapiens"
     def talk(self):
          return "Hello there, how are you?"

nobody = Person()
print(nobody.species)
print(nobody.talk())
