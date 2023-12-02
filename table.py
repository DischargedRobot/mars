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





