#Rewrite all_the_snacks function so that takes additional argument spacer.           
#Use + to combine your snack and spacer before multiplying. Test your function with different inputs
#Whats happends if you use both strings for snack and spacer? Both numbers? A string and an integer?

def all_the_snacks(snack, spacer):
    print((snack + spacer) * 10)

all_the_snacks('Chikki',' ')
all_the_snacks('Chikki',' is ')
all_the_snacks(50,2)

# TypeError: Can't convert 'int' object to str implicitly
# all_the_snacks('Chikki',20)

# TypeError: all_the_snacks() missing 1 required positional argument: 'spacer'
# all_the_snacks(50)
