# Write an extract_longer(length, sentence) function that takes a sentence and 
# word length, then returns a list of the sentence's words that exceed the given
# length, if no words match the length, return False.

def extract_longer(length, sentence):
    longer = []
    words = sentence.split()
    for i in sentence.split():
         if len(i) > length:
              longer.append(i)
    if (longer):
        return longer
    else:
        return False 

print(extract_longer(5,'Everybody likes bananas'))
print(extract_longer(10,'Everybody likes bananas'))

