#Write code to randomly select price from price list, round it to nearest integer and print the result.

import random
groceryPrices = [9.42, 5.67, 3.25, 13.40, 7.50] 
x = random.choice(groceryPrices)
print('Random Price = ', x) 
print('Rounded Price = ', round(x,0)) 
