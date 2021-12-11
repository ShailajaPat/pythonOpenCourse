class Person(object):
     species = "Homo sapiens"
     favorite_color = "black"

     def __init__(self, name="Unknown", age=18):
          self.name = name
          self.age = age
          
     def talk(self):
          return "Hello, my name is {}.".format(self.name)

class Employee(Person):
     def talk(self):
         talk_str = super(Employee, self).talk()
         return talk_str + " I work for {} ".format(self.employer)

fred = Employee("Fred Flintstone", 55)
fred.employer = "PTC India Pvt Ltd."

print(fred.talk())
