# Write a colour_swapper function which takes my_colour and neighbour_colour
# as inputs and prints a message declaring colours after swapping. Add a line 
# before the print that swaps the contents of the variable.
# How you were able to swap them in the function without swapping them in your notebook?
 
def colour_swapper(x, y):
    print('Function: Before swapping ',x,y)
    x, y = y, x
    print('Function: After swapping  ',x,y)

my_colour = input('Enter your favorite colour ')
neighbour_colour = input('Enter your neighbour\'s favorite colour ')
print('Notebook: Before swapping  ',my_colour, neighbour_colour)
colour_swapper(my_colour, neighbour_colour)
print('Notebook: After swapping  ',my_colour, neighbour_colour)
