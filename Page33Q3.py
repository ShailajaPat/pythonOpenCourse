#Modify an in_grocery_list to test if grocery_item is a string.
#Print a message warning the user it is not

def in_grocery_list(grocery_item):
    groceryList = ['Society Tea', 'Sugar', 'Wheat', 'Rice', 'Biscuits']
    if (type(grocery_item) != str):
        print('Please enter correct grocery item')
    elif (grocery_item in groceryList):
        print('Item present in list');
    else:
        print('Item not present in list');

in_grocery_list(100)
in_grocery_list('Wheat')
in_grocery_list('Chikki')
