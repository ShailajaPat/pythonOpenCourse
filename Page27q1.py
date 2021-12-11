# Write a function volume which computes and returns the volume of a box
# given the width, length and height
 
def volume(w,l,h):
    return (w*l*h)

width  = input('Enter width of box ')
length = input('Enter length of box ')
height = input('Enter height of box ')
print('Volume of box = ', volume(int(width), int(length), int(height)))
