# The outer loop tells us the number of rows, 
# and the inner loop tells us the column needed to print the pattern.

#NESTED LOOP BASICS
# * * * *
# * * * *
# * * * *
# * * * * Solution should look like these
 
for i in range(4):
    for  j in range(4):
        print("*", end = " ")
    print()


# PYRAMID PATTERNS OF NUMBERS
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5   Solution should look like these 

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end = " ")
    print()


# Inverted pyramid pattern of numbers
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5   Solution should look like these 

b = 0
for i in range(5,0,-1):
    b+= 1
    for j in range(1,i+1):
        print(b, end=" ")
    print()


