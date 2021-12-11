# Clearly your favorite snack is more important than the other items on list. 
# Modify your for loop to use break stop printing once you found favorite snack.
# Question: Could you acheive the same result without using a break?
# Bonus: if you snack isn't in the list, print a warning at the end

groceryList = ['Society Tea', 'Sugar', 'Wheat', 'Rice', 'Biscuits']

print('Using break : Buy: ')
for item in groceryList:
    print(item)
    if (item == 'Chikki'):
         break;
else: print('Chikki not in the list')

print('Witnout using break : Buy: ')
found = False
for item in groceryList:
    if (item == 'Chikki'):
         print(item)
         found = True;
    if (found == False):
         print(item)
         continue;
