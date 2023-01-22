# " what is instanciating in python"
# When a copy of a class is created that inherits all the class properties & functions, 
# it is called instantiating a class. 

class mobile:
    def alarm(self):          #alarm() is the behaviour of mobile i.e. method
        print("wake me at 5")
watch = mobile()              #here watch is the object of mobile.
watch.alarm()                 #object.method to get the output
mobile.alarm(watch)           #class.method(object)
print(type(watch))

# Special Method starts with __specialMethod__ i.e. __init__, __main__
# Role of __init__ is, The __init__ method lets the class initialize 
# the object's attributes and serves no other purpose. It is only used within classes.

class mobile:
    def __init__(self,memory,color):  #__init__ instantiate the object right when it is created
        self.memory = memory     #we created an attribute of the class mobile
        self.color= color
        print(memory)
        print(color)
samsung =mobile("5 gb","blue")
iphone = mobile("1 tb","pink")

#Different way of solving or getting output
class Beverage:
    def __init__(self,strong,loose):
        self.strong  = strong
        self.loose = loose
    def strong_coffee(self):
        return self.strong
    def loose_coffee(self):
        return self.loose
espresso = Beverage("edible","sweet")
print(espresso.strong_coffee())
americano = Beverage("edible","sweet")
print(americano.loose_coffee())


