import random


class Gene:

    def __init__(self):
        self.x = random.random() * 2 - 1
        self.y = random.random() * 2 - 1

    def copy(self, action):
        self.x = action.get_x()
        self.y = action.get_y()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def mutate(self):
        if random.random() < 0.8:
            self.x = random.random() * 2 - 1
        if random.random() < 0.8:
            self.y = random.random() * 2 - 1
