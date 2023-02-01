#Problem- 1 Print First 10 natural numbers using while loop
# i = 1
# while i <= 10:
#     print("The natural numbers are: " ,i)
#     i+=1


#Problem - 2 printing patterns
# print ("1")
# print ("1","2")
# print ("1","2","3")
# print ("1","2","3","4")
# print ("1","2","3","4","5")


# for i in range(1,6):
#     for j in range(1,6):
#         print(i, end= " ")
#     print('')


# for i in range(1,11):
#     for j in range(1,11):
#         print(i * j, end = ' ')
#     print()


# rows = 5
# for i in range(rows):
#     for j in range(i):
#         print(i, end = " ")
#     print(' ')


# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print('')


# rows = 5
# for i in range(1, rows ):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print('')


# rows = 6
# for rows in range(6):
#     for column in range(6,rows):
#         print(rows, end = " ")
#     print()
    
# for i in range(1,7):
#     for j in range(1,i+1):
#         print('@',end=' ')
#     print()

# for i in range(6,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# The outer loop tells us the number of rows, 
# and the inner loop tells us the column needed to print the pattern.

# PYRAMID PATTERNS OF NUMBERS
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5   Solution should look like these 

class NegativeAgeError(Exception):

    def __init__(self, age, message ):
        message = "Age should not be negative"
        self.age = age
        self.message = message

age = int(input("Enter age: "))
if age < 0:
    raise NegativeAgeError(age)

