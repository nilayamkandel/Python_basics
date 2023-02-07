# we used self to instantiate the object attribute here we will learn
#  the term used to define class attributes

class Person:
    max_person = 5

    def __init__(self,name):
        self.name = name

p1 = Person("bill")
p2 = Person("alex")

print(f"The number of max people allowed is : {Person.max_person}")
print(p1.max_person)   #here p1 is the object of class Person so when it is printed it is
# called as class.classAttribute which is p1 = Person so p1.max_person is Person.max_personso it gives result 5

# Another one

class Person:
    no_of_people = 0

    def __init__(self,name):
        self.name = name

Person.max_person = 4
p1 = Person("bill")
p2 = Person("alex")

print(f"The number of max people allowed is : {Person.max_person}")
print(p1.max_person) 

#Another one
class Person:
    no_of_people = 0

    def __init__(self,name):
        self.name = name
        Person.no_of_people += 1     #with these line we can calculate the number of object we have assigned.

p1 = Person("jack")
p2 = Person("jill")
p4 = Person("samy")
print(Person.no_of_people)
