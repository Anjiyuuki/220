from random import *
class Die:

    # Constructor
    def __init__(self, num_sides):
        # Instance Variables
        self.sides = num_sides
        self.value = 1

    # Method
    def get_value(self):
        return self.value

    def roll(self):
        new_value = randint(1, self.sides)
        self.value = new_value

