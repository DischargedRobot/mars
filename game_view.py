import pygame
from settings_view import GEOM, DI
from cube_view import CubeView
import random
from table_view import Tableview
class GameView:
    ''' отрисовка всей игры '''
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.table = Tableview(width, height)

    def redraw_table(self):
        self.table.table_disp.blit(self.table.table_img, (0,0))
    def redraw_cubes(self, cube_list = list()):
        ''' обновление изображения '''
        if len(cube_list) != 0:
            self.paint_Cube(cube_list)
        for cube in self.cubes_group:
            cube.paint(self.table.table_disp)
        pygame.display.update()
    def paint_Cube(self, cube_list: list()):
        self.cubes_group = pygame.sprite.Group()
        i = 0
        while len(self.cubes_group) < len(cube_list):
            cube = CubeView(random.randint(0,(self.width-self.width*0.3)),random.randint(0,self.height-self.height*0.3), cube_list[i])
            if not pygame.sprite.spritecollide(cube, self.cubes_group, False):
                i += 1
                self.cubes_group.add(cube)


