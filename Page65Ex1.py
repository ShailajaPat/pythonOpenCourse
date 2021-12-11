class Person(object):
     species = "Homo sapiens"
     favorite_color = "black"

     def __init__(self, name="Unknown", age=18):
          self.name = name
          self.age = age
          
     def talk(self):
          return "Hello, my name is {}.".format(self.name)

     def __str__(self):
          return "Name: {0}, Age: {1}".format(self.name,self.age)

     def __repr__(self):
          return "Person('{0}',{1})".format(self.name,self.age)

     def __eq__(self, other):
          return self.age == other.age

bob = Person("Bob", 33)
mark = Person("Mark", 33)
print(bob == mark)
