# Abstraction in python is defined as a process of handling complexity
#  by hiding unnecessary information from the user. 

def add(num1, num2):
        return num1 + num2
    
def sub(num1, num2):
        return num1 - num2

def mul(num1,num2):
        return num1 * num2
    
def div(num1, num2):
        return num1 * num2

print("Select any operation:\n"
    "1: Addition\n"
    "2: Subtraction\n" 
    "3: Multiply\n"
    "4: Divide\n")

choose_option = [1,2,3,4]
choose = (int(input(f"Select any one of the operations between {choose_option} :")))

if choose == choose_option:
        num1 = (int(input("Enter a number: ")))
        num2 = (int(input("Enter a number: ")))
else:
    print("Option unavailable")
    for i in choose_option:
        print(choose)
        if i != choose:
            continue
        

if choose == 1:
    print(num1, "+" ,num2, "=" ,add(num1,num2))

elif choose == 2:
    print(num1, "-" ,num2, "=" ,sub(num1,num2))

elif choose == 3:
    print(num1, "*" ,num2, "=" ,mul(num1,num2))

elif choose == 4:
    print(num1, "/" ,num2, "=" ,div(num1,num2))



   