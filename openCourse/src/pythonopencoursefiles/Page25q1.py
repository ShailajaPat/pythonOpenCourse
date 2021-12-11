#Rewrite all_the_snacks so that num and spacer have defaults of 100 and ', '.
#Using your favorite snack as input, try running your function with no additional input

def all_the_snacks(snack, spacer = ', ', num = 100):
    print((snack + spacer) * num)

all_the_snacks('Chikki')
all_the_snacks('Chikki',' is ',8)
all_the_snacks(50,7,10)

