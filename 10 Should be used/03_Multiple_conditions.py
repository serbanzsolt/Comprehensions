options = ["any", "apple", "hello", "world", "albany", "a", "y"]
valid_strings = []

for string in options:
    if len(string) <= 1:
        continue
    
    if string[0] != "a":
        continue
    
    if string[-1] != "y":
        continue
    
    valid_strings.append(string)
    
print(valid_strings)

# Multi-condition comprehension

# valid_strings = [string for string in options if len(string) >= 2 if string[0] == "a" if string[-1] == "y"]
valid_strings = [
    string
    for string in options
    if len(string) >= 2
    if string[0] == "a"
    if string[-1] == "y"
]
print(valid_strings)