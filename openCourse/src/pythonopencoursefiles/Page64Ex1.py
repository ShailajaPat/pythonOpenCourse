class Person(object):
     species = "Homo sapiens"
     favorite_color = "black"
     def __init__(self, name="Unknown", age=18):
          self.name = name
          self.age = age
          
     def talk(self):
          return "Hello, my name is {}.".format(self.name)

mark = Person("Mark", 33)
mark.favorite_color = "green"
print(mark.favorite_color)
