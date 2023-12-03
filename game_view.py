import pygame
from settings_view import GEOM, DI
from cube_view import CubeView
import random
class GameView:
    ''' отрисовка всей игры '''
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.table_disp = pygame.display.set_mode((width, height))
        self.table_img = pygame.image.load(DI['image']['table'])

    def redraw(self, display: pygame.Surface, cube_list = list()):
        ''' обновление изображения '''
        self.table_disp.blit(self.table_img, (0,0))
        if len(cube_list) != 0:
            for i in range(len(cube_list)):
                cube = CubeView(random.randint(0,500),random.randint(0,500), cube_list[i])
                cube.paint(display)
        pygame.display.update()


