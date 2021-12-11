#Write all_the_snacks function that takes snack (string) and uses the * operator
#using each of the items on your grocery list. 
#Whats happends if you enter a number into your function?

def all_the_snacks(snack):
    print(snack * 100)

groceryList = ['Society Tea', 'Sugar', 'Wheat', 'Rice', 'Biscuits']
for snack in groceryList:
    all_the_snacks(snack+' ')

all_the_snacks(50)
