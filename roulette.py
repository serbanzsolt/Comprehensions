import random

def párose(szám):
    if szám % 2 == 0:
        return "Páros"
    else:
        return "Páratlan"


score = {
    0 : [0, "Nulla", "0", "0", 0], 
    1 : ["Piros", párose(1), "1st 12", "1 to 18", 1] ,
    2 : ["Fekete", párose(2), "1st 12", "1 to 18", 2] ,
    3 : ["Piros", párose(3), "1st 12", "1 to 18", 3] ,
    4 : ["Fekete", párose(4), "1st 12", "1 to 18", 1] ,
    5 : ["Piros", párose(5), "1st 12", "1 to 18", 2] ,
    6 : ["Fekete", párose(6), "1st 12", "1 to 18", 3] ,
    7 : ["Piros", párose(7), "1st 12", "1 to 18", 1] ,
    8 : ["Fekete", párose(8), "1st 12", "1 to 18", 2] ,
    9 : ["Piros", párose(9), "1st 12", "1 to 18", 3] ,
    10 : ["Fekete", párose(10), "1st 12", "1 to 18", 1] ,
    11 : ["Fekete", párose(11), "1st 12", "1 to 18", 2] ,
    12 : ["Piros", párose(12), "1st 12", "1 to 18", 3] ,
    13 : ["Fekete", párose(13), "2nd 12", "1 to 18", 1] ,
    14 : ["Piros", párose(14), "2nd 12", "1 to 18", 2] ,
    15 : ["Fekete", párose(15), "2nd 12", "1 to 18", 3] ,
    16 : ["Piros", párose(16), "2nd 12", "1 to 18", 1] ,
    17 : ["Fekete", párose(17), "2nd 12", "1 to 18", 2] ,
    18 : ["Piros", párose(18), "2nd 12", "1 to 18", 3] ,
    19 : ["Piros", párose(19), "2nd 12", "19 to 36", 1] ,
    20 : ["Fekete", párose(20), "2nd 12", "19 to 36", 2] ,
    21 : ["Piros", párose(21), "2nd 12", "19 to 36", 3] ,
    22 : ["Fekete", párose(22), "2nd 12", "19 to 36", 1] ,
    23 : ["Piros", párose(23), "2nd 12", "19 to 36", 2] ,
    24 : ["Fekete", párose(24), "2nd 12", "19 to 36", 3] ,
    25 : ["Piros", párose(25), "3rd 12", "19 to 36", 1] ,
    26 : ["Fekete", párose(26), "3rd 12", "19 to 36", 2] ,
    27 : ["Piros", párose(27), "3rd 12", "19 to 36", 3] ,
    28 : ["Fekete", párose(28), "3rd 12", "19 to 36", 1] ,
    29 : ["Fekete", párose(29), "3rd 12", "19 to 36", 2] ,
    30 : ["Piros", párose(30), "3rd 12", "19 to 36", 3] ,
    31 : ["Fekete", párose(31), "3rd 12", "19 to 36", 1] ,
    32 : ["Piros", párose(32), "3rd 12", "19 to 36", 2] ,
    33 : ["Fekete", párose(33), "3rd 12", "19 to 36", 3] ,
    34 : ["Piros", párose(34), "3rd 12", "19 to 36", 1] ,
    35 : ["Fekete", párose(35), "3rd 12", "19 to 36", 2] ,
    36 : ["Piros", párose(36), "3rd 12", "19 to 36", 3] 
}

# print(score.keys())
eredmények = list(score.values())
print(type(eredmények))
print(eredmények[29])
# print(score.values())
# print(type(score.values()))


# def pörgetés() ->int:
#     return random.randint(0, 37)
    
    
    
# print("Válassz!")

# print("1. Szám")
# print("2. Szím")
# print("3. Páros-Páratlan")

# menü = int(input("Menüszám(1-3): "))
# while menü < 1 or menü > 3:
#     menü = int(input("Menüszám(1-3): "))

# if menü == 1:
#     szám = int(input("Adj meg egy számot(0-36): "))

#     while szám < 0 or szám > 36:
#         print("Nem 0-36 közöttit adtál meg!")
#         szám = int(input("Szám(0-36): "))
        
#     pörgetés = pörgetés()
    
#     if pörgetés == szám:
#         print(f"{pörgetés}, NYERTÉL!")
#     else:
#         print(f"{pörgetés}, NEM NYERTÉL!")

# elif menü == 2:
#     print("készül") #színes
# else:
#     print("készül") #páros-páratlan