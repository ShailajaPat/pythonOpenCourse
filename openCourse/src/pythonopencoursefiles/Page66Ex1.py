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

tyler = Student("Tyler", 19)

print(tyler.species)

print(tyler.talk())

tyler.do_homework()
