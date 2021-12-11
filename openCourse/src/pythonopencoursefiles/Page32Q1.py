# Write a you_own function that randomly picks a number from your price list
# [9.42, 5.67, 3.25, 13.40, 7.50] and prints True or False depending on whether the random number is greater than 10

import random

def you_own():
    groceryPrices = [9.42, 5.67, 3.25, 13.40, 7.50]
    x = random.choice(groceryPrices)
    print(x)
    return x > 10 

print(you_own())
print(you_own())
