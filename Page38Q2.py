# Use enumerate to print out a numbered grocery list.
# There are often several diff ways to get the same o/p. However, usually one is more elegant than the others. 

groceryList = ['Society Tea', 'Sugar', 'Wheat', 'Rice', 'Biscuits']

print('Note to self: Buy: ')
for (i, j) in enumerate(groceryList):
    print(i+1,' ',j)
