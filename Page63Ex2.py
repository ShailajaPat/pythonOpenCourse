class Person(object):
     species = "Homo sapiens"
     def __init__(self, name="Unknown", age=18):
          self.name = name
          self.age = age
          
     def talk(self):
          return "Hello, my name is {}.".format(self.name)

mark = Person("Mark", 33)
generic_voter = Person()
generic_worker = Person(age=41)
print(generic_worker.age)
print(generic_worker.name)
