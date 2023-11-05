from cup import Cup
from cube import Cube
import copy

class Table:

    def __init__(self):
        self.table = []
        self.hand = []

    def put_aside(self):
        self.hand = Cup().cast()
        for i in range(len(self.hand)):
            if self.hand[i] == 'танк':
                self.table.append(self.hand[i])