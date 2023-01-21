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


