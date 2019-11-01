# it should have a name, phone, email, location, speciality
#
# 3) have method see patients, that takes in an argument and returns 'THIS PATIENT IS CURED, off you go <dog's name>'


class vets:

    def __init__(self,name,phone,email,location,speciality):
        self.name = name
        self.phone = phone
        self.email = email
        self.location = location
        self.speciality = speciality

    def seepatients(self):
        return "this partient is" + cured + "off you go" + dog1.name

