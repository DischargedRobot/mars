from cube import Cube
import random

class Cup:
    """ Стаканчик с кубиками"""
    def __init__(self, numbers: int = 13, new: int = 0):
        self.cow = 0
        self.laser = 0
        self.chiken = 0
        self.people = 0
        self.tank = 0
        if new == 1:
            self.list_cup = [Cube for i in range(13)]
        else:
            self.numbers = numbers
        # print(self.list_cup)
    def __repr__(self):
        return f'Количество кубиков: {len(self.list_cup)}'

    # бросок кубиков
    def cast(self):
        self.list_cup = [Cube().sides[random.randint(0,5)] for i in range(self.numbers)]
        return self.list_cup






