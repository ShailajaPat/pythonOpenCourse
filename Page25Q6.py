#Challenge: Modify price_matcher function to return item, price ranthe than print them
#Write a free_charge function that calls your price_matcher and uses the result to 
#print your item and the absolute value of the change for the item assuming you paid $

import random

def price_matcher():
    x = random.randint(0,4)
    return groceryList[x], groceryPrices[x]

def free_charge():
    item, price = price_matcher()
    print(item, price, abs(10-price))

groceryPrices = [9.42, 5.67, 3.25, 13.40, 7.50] 
groceryList = ['Society Tea', 'Sugar', 'Wheat', 'Rice', 'Biscuits']

free_charge()
