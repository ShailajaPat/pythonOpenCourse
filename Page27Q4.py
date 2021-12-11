# Write a global_colour_swapper function that swaps colours globally
# Run your function and then print colours
 
def global_colour_swapper():
    global my_colour, neighbour_colour
    print('Function: Before swapping ',my_colour, neighbour_colour)
    my_colour,  neighbour_colour =  neighbour_colour, my_colour
    print('Function: After swapping  ',my_colour, neighbour_colour)

my_colour = input('Enter your favorite colour ')
neighbour_colour = input('Enter your neighbour\'s favorite colour ')
print('Notebook: Before swapping  ',my_colour, neighbour_colour)
global_colour_swapper()
print('Notebook: After swapping  ',my_colour, neighbour_colour)
