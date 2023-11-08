from cup import Cup
from cube import Cube
import copy

class Table:
    """ Игровой стол """
    def __init__(self):
        self.cow = 0
        self.laser = 0
        self.chiken = 0
        self.people = 0
        self.tank = 0
        self.table = {"Танки": self.tank}
        self.hand = Cup()
        self.tank = 0
        na_koroble = {'people': 0, 'chiken': 0, 'cow': 0, 'laser': 0, }

    # бросок и отбор танков
    def put_aside(self):
        self.hand.cast()
        self.hand.tank = self.hand.list_cup.count("танк")
        self.tank += self.hand.tank
        self.hand.numbers -= self.hand.tank
        self.hand.cow = self.hand.list_cup.count("корова")
        self.hand.laser = self.hand.list_cup.count("лазер")
        self.hand.chiken = self.hand.list_cup.count("курица")
        self.hand.people = self.hand.list_cup.count("человек")
