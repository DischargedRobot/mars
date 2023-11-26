from cup import Cup
from cube import Cube
from table import Table
from game import Game

game = Game()
while True:
    action = input('1) Бросить кубики\n2) Посмотреть содержимое тарелки\n')
    game.step(action)
    if game.table.plate['танк'] > game.table.plate['лазер'] + game.cup.numbers:
        print('end')
        break
