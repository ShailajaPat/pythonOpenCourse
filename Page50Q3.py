# Write a function that takes a portion mark as input and returns the full 
# classification 
# convert_classification('U//FOUO') should return 'UNCLASSIFIED//FOR OFFICIAL USEONLY'
# convert_classification('S//REL TO USA, FVEY')  'SECRET//REL TO USA, FVEY'

def convert_classification(original):
    expanded  = []
    for i in original:
         if original.count(i) > 1:
              if i not in duplicate:
                  duplicate.append(i)
    if (duplicate):
        return duplicate
    else:
        return False 

print(duplicates([1,2,3,6,7,3,4,5,6])) # should return [3,6]
print(duplicates(['cow','pig','goat','horse','pig'])) # should return ['pig']
