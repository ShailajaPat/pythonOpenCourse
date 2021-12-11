# Write a function isDivisibleBy(num,divisor) to check if a number is evenly divisible by divisor
# 

def isDivisibleBy(num, divisor):
    return((num % divisor) == 0)

print(isDivisibleBy(21, 7))
print(isDivisibleBy(25, 5))
print(isDivisibleBy(100, 21))

