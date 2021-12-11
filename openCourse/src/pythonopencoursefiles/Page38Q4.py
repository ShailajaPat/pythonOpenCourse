# Challenge: Write a "guess my number" game that generates a random number
# use input to get use guesses. 

import random

for i in range(5):
    x = random.randint(0,100)
    y1 = input('Enter a number between 0 to 100 ')
    try:
         y = int(y1)
         if (x == y):
              print('You guessed right!',x)
         else:
              print('Random number was ',x) 
    except ValueError:
         print('please enter a number')
