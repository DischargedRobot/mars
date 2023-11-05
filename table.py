from cup import Cup
from cube import Cube
import copy

class Table:

    def __init__(self):
        self.table = []
        self.hand = Cup()

    def put_aside(self):
        self.hand.cast()
        for i in range(len(self.hand.list_cup)):
            if self.hand.list_cup[i] == 'танк':
                self.table.append(self.hand.list_cup[i])
                self.hand.numbers -= 1
