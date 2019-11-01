from animal import *

class reptile(animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self. heart_chambers = [3,4]
        self.amniotic_eggs = None

    def seek_heat(self):
        return("its chilly outside, where is the sun")

    def hunt(self):
        return "wait for it, wait for it....and pounce"

    def use_venom(self):
        return("ive got it Im using it")
    def temp_regulation(self):
        return "hot n cold"




snake = reptile()
print(snake.hunt())

print(snake.seek_heat())

print(snake.temp_regulation())

print(snake.communicate())