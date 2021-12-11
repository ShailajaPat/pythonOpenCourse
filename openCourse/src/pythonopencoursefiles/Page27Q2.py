# Use input to ask your favorite number and store it in variable my_num
# Run 2 + my_num. Why does this fail? How can you fix it?
# 
my_num = input('Enter your favorite number ')
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(2 + my_num) 

print(2 + int(my_num)) 
