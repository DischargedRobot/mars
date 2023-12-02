from cup import Cup
from cube import Cube
from table import Table
from game import Game

game = Game()
while True:
    action = input('1) Бросить кубики\n2) Посмотреть содержимое тарелки\n3) Закончить раунд\n')
    if action == '3':
        print(f'{game.score()}Конец вашего раунда')
        break
    else:
        game.step(action)
        if game.table.plate['танк'] > game.table.plate['лазер'] + game.cup.numbers:
            print('Поражение')
            break
        elif game.cup.numbers == 0:
            print(f'{game.score()}Конец вашего раунда')
            break


