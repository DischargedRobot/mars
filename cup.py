from cube import Cube
import random

class Cup:
    """ Стаканчик с кубиками"""
    def __init__(self, numbers: int = 13):
        self.numbers = numbers
        self.list_cup = []

    def __repr__(self):
        return f'Количество кубиков: {self.numbers}'

    # бросок кубиков
    def cast(self):
        self.list_cup = [Cube(random.randint(0,5)).creature for i in range(self.numbers)]
        return self.list_cup

    def delite_creature(self, creature):
        for i in range(self.list_cup.count(creature)):
            self.list_cup.remove(creature)
        return self.list_cup







