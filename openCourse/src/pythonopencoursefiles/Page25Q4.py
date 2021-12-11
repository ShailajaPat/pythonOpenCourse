#Write in_grocery_list function that takes in a grocery_item returns True or False
#depending on whether the item in your list.   

def in_grocery_list(grocery_item):
    return(grocery_item in groceryList)

groceryList = ['Society Tea', 'Sugar', 'Wheat', 'Rice', 'Biscuits']

print(in_grocery_list('Rice'))

print(in_grocery_list('chocolate'))
