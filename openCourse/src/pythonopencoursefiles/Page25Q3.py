#Rewrite all_the_snacks function so that it also takes argument num.           
#Lets you customize the number of times your snack gets printed out.

def all_the_snacks(snack, spacer, num):
    print((snack + spacer) * num)

all_the_snacks('Chikki',' ',5)
all_the_snacks('Chikki',' is ',8)
all_the_snacks(50,7,10)

