
from game import Game

import pygame

clock = pygame.time.Clock()
game = Game()

game.table_view.redraw_action_of_player()
pygame.display.update()
game.run()


