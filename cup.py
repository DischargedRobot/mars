from cube import Cube
import random

class Cup:

    def __init__(self, new: int = 0):
        if new == 1:
            self.list_cup = [Cube for i in range(13)]
        # print(self.list_cup)
    def __repr__(self):
        return f'Количество кубиков: {len(self.list_cup)}'

    def cast(self):
        self.list_cup = [Cube().sides[random.randint(0,5)] for i in range(13)]
        return self.list_cup






