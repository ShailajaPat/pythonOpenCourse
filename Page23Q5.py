#Challenge: Your grocery store has weird promotion called "win free change"
#A rendom item from your grocery prices is chosen and you have to pay $10
#If item is less than 10$ you get the item and change back as normal
#However, if you are lucky and price is greater than 10$ you get item and difference in price back as change
#Write code to randomly pick a price and display the amount of change the cashier has to pay you during this prmotion
#Hint: use built-in abs function

import random

groceryPrices = [9.42, 5.67, 3.25, 13.40, 7.50] 
x = random.choice(groceryPrices)
print('Random Price = ', x) 
print('You get change = ', round(abs(10 - x),2))
