import random

def square(x):
    x = x**2
    return x

def is_even(x):
    if x % 2 == 0:
        return "EVEN"
    else:
        return "ODD"
    
cycle = random.randint(1, 1000)
print(cycle)

# numbers_squared = [square(x) for x in range(cycle) ]
# print(numbers_squared)
numbers_squared = [(is_even(square(x+1)), x, )for x in range(cycle) ]
print(numbers_squared)