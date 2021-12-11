class Person(object):
     species = "Homo sapiens"
     favorite_color = "black"

     def __init__(self, name="Unknown", age=18):
          self.name = name
          self.age = age
          
     def talk(self):
          return "Hello, my name is {}.".format(self.name)

def person_str(self):
    return "Name: {0}, Age: {1}".format(self.name,self.age)

def person_repr(self):
    return "Person('{0}',{1})".format(self.name,self.age)

def person_eq(self, other):
    return self.age == other.age

Person.__str__ = person_str
Person.__repr__ = person_repr
Person.__eq__ = person_eq

bob = Person("Bob", 33)
mark = Person("Mark", 33)
print(bob == mark)
