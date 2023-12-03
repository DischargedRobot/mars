class Cube:
    """ Кубик """

    def __init__(self, number):
        self.sides = {0: 'корова', 1: 'человек', 2: 'человек', 3: 'курица', 4: 'лазер', 5: 'танк'}
        self.creature = self.sides[number]

    def __repr__(self):
        return f'{self.creature}'

print(repr(Cube(0)))
