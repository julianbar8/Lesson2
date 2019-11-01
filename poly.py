from reptile import *

class lizard(reptile):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.venom = None
        self.limbs = False

    def use_tongue_to_smell(self):
        return "do I say it smeells or tastes nice...?"

sidney = lizard()
print(sidney.seek_heat())

simon = lizard()
print(simon.use_tongue_to_smell())
