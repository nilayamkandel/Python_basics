#Static methods are used when we don't want subclasses of a class 
# change/override a specific implementation of a method.

class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("run")

print(Math.add5(5))  #class.method came directly.
print(Math.add10(10))
Math.pr()
    
