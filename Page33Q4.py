# Challege: Re-write the you_won function to randomly choose a number from
# [9.42, 5.67, 3.25, 13.40, 7.50] and prints message depending on whther you own
# also include amount of change you will be receiving in your message.

import random

def you_own():
    groceryPrices = [9.42, 5.67, 3.25, 13.40, 7.50]
    x = random.choice(groceryPrices)
    print(x)
    if (x > 10):
        print('You own ', round(x - 10, 2))
    print('End of function') 

you_own()
