# multiple inheritance example
class Person(object):
     species = "Homo sapiens"
     favorite_color = "black"

     def __init__(self, name="Unknown", age=18):
          self.name = name
          self.age = age
          
     def talk(self):
          return "Hello, my name is {}.".format(self.name)

class Student(Person):
     bedtime = 'Midnight'
     
     def do_homework(self):
         import time
         print("I need to work ")
         time.sleep(5)
         print("Did I just fall asleep?")

class Employee(Person):
     def __init__(self, name, age, employer):
          super(Employee, self).__init__(name, age)
          self.employer = employer
     def talk(self):
         talk_str = super(Employee, self).talk()
         return talk_str + " I work for {} ".format(self.employer)

class StudentEmployee(Student, Employee):
     pass

ann = StudentEmployee("ann", 58, "Family Services")

print(ann.talk())

# TypeError: __init__() missing 1 required positional argument: 'employer`
# bill = StudentEmployee("bill", 20)
# Corrected as follows -
bill = StudentEmployee("bill", 20, "Telco, Pimpri")
