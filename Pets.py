# dogs should have a name, owner and age.
#
# 5) dogs should be able to: bark, eat, sleep
class Pets:
    def __init__(self,name,owner,age,status):
        self.name = name
        self.owner = owner
        self.age = age


    def bark(self):
        return("wooof")

    def sleep(self):
        return ("zzz")

    def eat(self):
        return("nom nom nom")

Dog1 = Dog("Max","Julian", 9,"cured")
Dog2 = Dog("Tom","Maf", 5,"not cured")
Dog3 = Dog("Jak","Isabella", 3,"cured")