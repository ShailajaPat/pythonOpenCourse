# Using shout function, write a shout_words(sentence) fucntion that takes
# a string argument and "shouts" each word on its own line.

def shout(str):
    return(str.upper()+'!')

def shout_words(sentence):
    words = sentence.split()
    for i in sentence.split():
         print(shout(i))

print(shout_words('Everybody likes bananas'))

#print(shout('Bananas'))
#print(shout('hello world'))

