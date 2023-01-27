# create a function that takes input
# create a function that evaluates two number
# the argument of evaluate function should take two inputs along with the condition to evaluate
# eg:- evaluate (num1,num2,condition)
# create a variable that stores the existing condition for infinite loop
# create a infinite loop 
# take two number as input and pass it to evaluate function
# print result
# take an input to confirm you want to exit
# check if you want to end the infiinite loop 

def user_input(isNumber = True ,isExit = False):
    if not isExit:
        input_type = ""
        if isNumber:
            input_type = "number"
        else:
            input_type = "condition"
        return(input("Enter the "+ input_type + ": "))
    else:
        return(input("Type YES to exit, NO to continue: "))
       
def calc_evaluate(num1,num2,condition):
    num1 = int(num1)
    num2 = int(num2)
    if condition == "+":
        return(num1 + num2)
    elif condition == "-":
        return(num1 - num2)    
    elif condition == "*":
        return(num1 * num2)   
    elif condition == "/":
        return(num1 / num2)    
    else:
        print("invalid condition")
        
def calculator():
    isExit = "NO"
    while(isExit == "NO"):
        result = calc_evaluate(user_input(),user_input(),user_input(False))
        print("Result: " , result)
        isExit = user_input(isExit = True)

calculator()

