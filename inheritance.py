# Inheritance allows us to define a class that inherits all the methods and 
# properties from another class. Parent class is the class being inherited from,
# also called base class. Child class is the class that inherits from another class,
#also called derived class.MORE INFO ON "https://www.geeksforgeeks.org/inheritance-in-python/"




# PROGRAM WITHOUT INHERITANCE
class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    print("bark")

    def get_name(self):
        return self.name
#  here we can see that the attribute name,age both are same in both class.
#  using this again and again just make code longer so we use inheritance to do code reusability
class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    print("meow")

d1 = dog("tommy",3)
print(dog.get_name(d1))





#PROGRAM WITH INHERITANCE
class animals:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age}years old")

class dog(animals):
    def speak(self):
        print("I can bark")

class cat(animals):
    def speak(self,voice):
        self.voice = voice
        print("I do meow")

a = animals("tommy",5)
a.show()
d1 = dog("lucky",8)
d1.show()
# d1.speak()
# print(f"Here is my identity {d1.show()} and i can {d1.speak()}")


# USE OF SUPER METHOD
class animals:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age}years old")

    def speak(self):
        print("i speak good language")

class dog(animals):
    def speak(self):
        print("I can bark")

    def __init__(self,name,age,color):
        super().__init__(name,age,color)
        self.color = color

    def show(self):
        print(f"I am {self.name} and I am {self.age}years old and i am {self.color}in color.")

class cat(animals):
    def speak(self):
        print("I do meow")

class fish(animals):
    pass

a = animals("tommy",5)
a.show()
d1 = dog("lucky",8,"brown")
d1.show()
f = fish("tim",3)
f.speak()

