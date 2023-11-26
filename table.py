from cup import Cup
from cube import Cube
import copy
from prettytable import PrettyTable

class Table:
    """ Игровой стол """
    def __init__(self):
        self.dice_on_table = {'человек': 0, 'курица': 0, 'корова': 0, 'лазер': 0, 'танк': 0}
        self.plate = {'человек': 0, 'курица': 0, 'корова': 0, 'лазер': 0, 'танк': 0 }

    def __repr__(self):
        return str(self.dice_on_table)

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


