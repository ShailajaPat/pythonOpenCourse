# Using for loop and enumerate, write a function getindex(string,char)
# to recreate the string method .index

def getindex(text, ch):
     for (i,j) in enumerate(text):
         if (j == ch):
              return i
     return -1

print(getindex('skyscraper', 'c'))
