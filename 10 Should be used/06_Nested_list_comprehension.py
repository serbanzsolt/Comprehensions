import pprint

printer = pprint.PrettyPrinter()

lst = []

for a in range(5):
    l1 = []
    for b in range(5):
        l2 = []
        for c in range(5):
            l2.append(c)
        l1.append(l2)
    lst.append(l1)
    
printer.pprint(lst)

lst2 = [[[c for c in range(5)] for _ in range(5)] for _ in range(5)]
printer.pprint(lst2)