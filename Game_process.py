import pygame

from cup import Cup
from cube import Cube
from table import Table
from game import Game
from game_view import GameView
from settings_view import GEOM
import pygame

clock = pygame.time.Clock()
game = Game()
gameview = GameView(GEOM['display'][0], GEOM['display'][1])
size = GEOM['display']
display = pygame.display.set_mode(size)
gameview.redraw(display)
while True:
    action = input('1) Бросить кубики\n2) Посмотреть содержимое тарелки\n3) Закончить раунд\n')
    if action == '3':
        print(f'{game.score()}Конец вашего раунда')
        break
    else:
        game.step(action)
        gameview.redraw(display,game.cup.list_cup)
        if game.table.plate['танк'] > game.table.plate['лазер'] + game.cup.numbers:
            print('Поражение')
            break
        elif game.cup.numbers == 0:
            print(f'{game.score()}Конец вашего раунда')
            break
    clock.tick(24)

