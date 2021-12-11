#Write price_matcher function that takes no argument, but prints a random grocery item and a random price from your price list every time it is run

import random

def price_matcher():
    print('Item  = ', random.choice(groceryList))
    print('Price = ', random.choice(groceryPrices))

groceryPrices = [9.42, 5.67, 3.25, 13.40, 7.50] 
groceryList = ['Society Tea', 'Sugar', 'Wheat', 'Rice', 'Biscuits']

price_matcher()
