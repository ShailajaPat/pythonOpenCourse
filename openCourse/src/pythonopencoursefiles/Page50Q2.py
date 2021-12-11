# Write a function that takes a list as a parameter and returns a second list
# composed of any objects that appear more than once in the original list
# duplicates([1,2,3,6,7,3,4,5,6]) should return [3,6]

def duplicates(original):
    duplicate = []
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
