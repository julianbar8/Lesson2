# #a classs is a "blueprint " for creeating objects
# #creating class
#
# class Dog:
#     animal_kind = "canine"
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     #adding method
#     def bark(self):
#         return("wooof")
#
#     def run(self):
#         return ("fast")
#     def eat(self):
#         return("a lots")
#
# #instantiation of objects
#
# Dog1 = Dog("Max", 9)
# Dog2 = Dog("Tom", 5)
#
# print(type(Dog1))
# print(Dog1.animal_kind)
# #calling methods
# print(Dog2.bark())
# print(Dog1.run())
# print(Dog2.eat())
#
# print(Dog1.name)
# print("{} is {} years old".format(Dog1.name,Dog1.age))
#
#
#a classs is a "blueprint " for creeating objects
#creating class

class Dog:
    animal_kind = "canine"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #adding method
    def bark(self):
        return("wooof")

    def run(self):
        return ("fast")
    def eat(self):
        return("a lots")

#instantiation of objects

Dog1 = Dog("Max", 9)
Dog2 = Dog("Tom", 5)
Dog3 = Dog("Jak", 3)

print(type(Dog1))
print(Dog1.animal_kind)
#calling methods
print(Dog2.bark())
print(Dog1.run())
print(Dog2.eat())

print(Dog1.name)
print("{} is {} years old".format(Dog1.name,Dog1.age))

print("Dog1 age is greater than Dog2 : ", Dog1.age > Dog2.age, Dog3.age)
print("Dog1 age is greater than Dog3 : ", Dog1.age > Dog3.age)
print("Dog2 age is greater than Dog3 : ", Dog2.age > Dog3.age)
print("Dog3 age is greater than Dog2 : ", Dog3.age > Dog2.age)

max(Dog1.age,Dog2.age,Dog3.age)


#1. Fizzbuzz using functions 2.Using functions check whether the given year is a leap year 