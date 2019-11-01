#abstraction mean hiding complexity and showing essential features of objects

#Inheritence allows us to define class that inherits all the methods and properties from another class

# Encapsulation is an internal representation of an object that will not be shown to the user ( it is higly level of abstractions )

# polymorphism refers to adabtibility of object to adapt to the code 
class animal():

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return ("one breath in, one breath out")

    def eat(self,food):
        return("nom nom nom")

    def sleep(self):
        return "zzzz and snoring"
    def communicate(self):
        return "pass the information to survive"

