# Use range to write a for loop to print out a numbered grocery list

groceryList = ['Society Tea', 'Sugar', 'Wheat', 'Rice', 'Biscuits']

print('Note to self: Buy: ')
for i in range(1,len(groceryList)+1):
    print(i,' ',groceryList[i-1])
