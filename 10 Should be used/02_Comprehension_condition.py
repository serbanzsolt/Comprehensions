evens = []
for number in range(50):
    is_even = number % 2 == 0
    if is_even:
        evens.append(number)
print(evens)

# Using a Comprehension
evens = [number for number in range(50) if number % 2 == 0]
print(evens)