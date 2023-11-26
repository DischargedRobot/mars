from cube import Cube
import random

class Cup:
    """ Стаканчик с кубиками"""
    def __init__(self, numbers: int = 13):
        self.numbers = numbers

    def __repr__(self):
        return f'Количество кубиков: {len(self.list_cup)}'

    # бросок кубиков
    def cast(self):
        self.list_cup = [Cube().sides[random.randint(0,5)] for i in range(self.numbers)]
        return self.list_cup






