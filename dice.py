#generate dice

import random

#defining variables
a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "

def randomnumber():
    num1 = random.randint(1, 6)
    return num1

def board():
    print(f" {a} | {b} | {c} ")
    print("-----------")
    print(f" {d} | {e} | {f} ")
    print("-----------")
    print(f" {g} | {h} | {i} ")

while True:
    
    x = input("Press p to play and s to exit: ")
    num2 = randomnumber()
    
    if x.lower() == "p":
        if num2 == 1:
            a = " "
            b = " "
            c = " "
            d = " "
            e = "O"
            f = " "
            g = " "
            h = " "
            i = " "
            
            print(num2)
            board()
            
        elif num2 == 2:
            a = "O"
            b = " "
            c = " "
            d = " "
            e = " "
            f = " "
            g = " "
            h = " "
            i = "O"
            print(num2)
            board()
            
        elif num2 == 3:
            a = "O"
            b = " "
            c = " "
            d = " "
            e = "O"
            f = " "
            g = " "
            h = " "
            i = "O"
            print(num2)
            board()
            
        elif num2 == 4:
            a = "O"
            b = " "
            c = "O"
            d = " "
            e = " "
            f = " "
            g = "O"
            h = " "
            i = "O"
           
            print(num2)
            board()
            
        elif num2 == 5:
            a = "O"
            b = " "
            c = "O"
            d = " "
            e = "O"
            f = " "
            g = "O"
            h = " "
            i = "O"
            print(num2)
            board()
            
        elif num2 == 6:
            a = "O"
            b = " "
            c = "O"
            d = "O"
            e = " "
            f = "O"
            g = "O"
            h = " "
            i = "O"
            print(num2)
            board()
            

    elif x.lower() == "s":
        break
    
    else:
        print('Press Valid character')


