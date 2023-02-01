# the "try" event detect and throw the exception while 
# "except" catches and handle the exception.It is the event that occurs during 
# the execution of program that disrupt the normal flow of execution
# they are usually used for the condition where user may enter the wrong input and 
# itmay be the reason for disruption to whole program being executed


# ============================================================================================
# PROBLEM 1
try:
    num = int(input("Enter the number : "))
except:                                       
    print("please enter only integer value")
print("------------------------------------------------------------------------------------------------------------------------------------------")
# =====================================================================================================


# what if the "except" have to accept multiple errors???
# depenidng on what may happen we can give the exception to catch the error.

# ===========================================================================================================
# PROBLEM 2
try:
    num = int(input("Enter the number : "))
    print(num)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("only enter integer")
print("----------------------------------------------------------------------------------------------------------------------------")
# ==============================================================================================================================

# 

# ===========================================================================================================================
# PROBLEM 3
# we can givemultiple exceptions using tuples
try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("The answer of a divide by b:", c)
except(ValueError, ZeroDivisionError):
    print("Please enter a valid value")
print("----------------------------------------------------------------------------------------------------------")

# ===============================================================================================================================
# we can use finally event to do clean-up action. Finally is used when we want to run the code at anycost
# PROBLEM 4
try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("The answer of a divide by b:", c)

except ZeroDivisionError:
    print("Can't divide with zero")
finally:
    print("Inside a finally block")

# ==========================================================================================================================
# using try-else statement
#  PROBLEM 5
try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("a/b = %d" % c)

except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("We are in else block ")
# ===================================================================================================================

# raising an exception. syntax= raise exception class(value)
# PROBLEM 6 
def simple_interest(amount, year, rate):
    try:
        if rate > 100:
            raise ValueError(rate)
        interest = (amount * year * rate) / 100
        print('The Simple Interest is', interest)
        return interest
    except ValueError:
        print('interest rate is out of range', rate)

print('Case 1')
simple_interest(800, 6, 8)

print('Case 2')
simple_interest(800, 6, 800)

# =====================================================================================================================
# Exception chaining 
# PROBLEM 7
try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a/b
    print("The answer of a divide by b:", c)
except ZeroDivisionError as e:
    raise ValueError("Division failed") from e
# ==================================================================================================================
# Custom and User-defined exceptions
# PROBLEM 8
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmallError(Error):
    """Raised when the input value is small"""
    pass

class ValueTooLargeError(Error):
    """Raised when the input value is large"""
    pass

while(True):
    try:
        num = int(input("Enter any value in 10 to 50 range: "))
        if num < 10:
            raise ValueTooSmallError
        elif num > 50:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
            print("Value is below range..try again")

    except ValueTooLargeError:
            print("value out of range...try again")

print("Great! value in correct range.")
# =========================================================================================================================
# PROBLEM 9
class NegativeAgeError(Exception):

    def __init__(self, age, ):
        message = "Age should not be negative"
        self.age = age
        self.message = message

age = int(input("Enter age: "))
if age < 0:
    raise NegativeAgeError(age)


