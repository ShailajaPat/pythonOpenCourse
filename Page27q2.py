# Write a function volume2 which calculates the box volume, assuming the height is 1 if not given.
 
def volume(w,l,h=1):
    return (w*l*h)

width  = input('Enter width of box ')
length = input('Enter length of box ')
print('Volume of box = ', volume(int(width), int(length) ))
height = input('Enter height of box ')
print('Volume of box = ', volume(int(width), int(length), int(height) ))
