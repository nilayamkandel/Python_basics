# The try block lets you test a block of code for errors. 
# The except block lets you handle the error.
# they are usually used for the condition where user may enter the wrong input and 
# itmay be the reason for disturbance to whole program being executed

try:
    num = int(input("Enter the number : "))
except:
    print("please enter only integer value")

