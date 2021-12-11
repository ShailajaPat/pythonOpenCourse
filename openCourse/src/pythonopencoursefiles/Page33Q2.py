#Write an in_grocery_list function that takes in a grocery_item and 
# prints an appropriate response depending on whether grocery_item is in your grocery list.

def in_grocery_list(grocery_item):
    groceryList = ['Society Tea', 'Sugar', 'Wheat', 'Rice', 'Biscuits']
    if (grocery_item in groceryList):
        print('Item present in list');
    else:
        print('Item not present in list');

in_grocery_list('Wheat')
in_grocery_list('Chikki')
