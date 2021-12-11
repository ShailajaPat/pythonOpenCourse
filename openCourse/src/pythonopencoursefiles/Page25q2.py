#Try running all_the_snacks with your favorite snack and the spacer '| '.
#How would you run it while inputing your favorite snack and 42 for num while keeing the default for spacer?
#Can you use this method to enter spacer and num in reverse order?

def all_the_snacks(snack, spacer = ', ', num = 100):
    print((snack + spacer) * num)

all_the_snacks('Chikki', spacer = '| ')
all_the_snacks('Chikki', num = 42)
all_the_snacks('Biscuits', num = 10, spacer = '* ')

