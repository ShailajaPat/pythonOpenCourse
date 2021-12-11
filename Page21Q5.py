#Using fast swapping exchange your favorite snack with neighbour's snack.
#Print both variables before and after swapping to see the result.
mySnack = 'Chikki'
neighbourSnack = 'Biscuits'
print('Before swap \nMy favorite snack = ',mySnack, '\nNeighbour\'s favorite snack = ',neighbourSnack)
mySnack, neighbourSnack = neighbourSnack, mySnack 
print('After swap \nMy favorite snack = ',mySnack, '\nNeighbour\'s favorite snack = ',neighbourSnack)
