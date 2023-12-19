import pygame
import os
import random
from settings_view import GEOM, DI
from cube import Cube

class CubeView(pygame.Rect):
    ''' отрисовка кубика'''
    size = (width, height) = GEOM['cube']
    size_display = (width_display, height_display) = GEOM['display']
    razmer = [width_display*0.30, height_display*0.30]


    def __init__(self, x: int, y: int, cube: str, number: int):
        super().__init__((x,y), (self.width,self.height))
        self.cube = cube
        self.creatures = {'человек': 0, 'курица': 1, 'корова': 2, 'лазер': 3, 'танк': 4}
        self.list_cube_tanks_coordinats = [(self.width_display*0.74+self.width),
                                            (self.height*1.5*(self.creatures[cube]+1))]
        self.list_cube_tanks_size = [self.razmer[0] * (1 / 13), self.razmer[1] * (1 / 13)]
        self.number = number
        # Координаты куба
        self.x = x
        self.y = y
        # перемещение куба
        self.x_motion = self.list_cube_tanks_coordinats[0] - self.x
        self.y_motion = self.list_cube_tanks_coordinats[1] - self.y
        img = pygame.image.load(DI['image']['cube'].format(repr(cube).replace("'",'')))
        self.image = pygame.transform.scale(img, self.size)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        # self.cube = pygame.sprite.Sprite(self.image, (self.x, self.y))

    def paint(self, display: pygame.Surface):
        display.blit(self.image, (self.x, self.y))

    def tank_motion(self):
        self.x += (self.x_motion)*0.0166
        self.y += (self.y_motion)*0.0166




