import pygame
import os
import random
from settings_view import GEOM, DI
from cube import Cube

class CubeView(pygame.sprite.Sprite):
    ''' отрисовка кубика'''
    size = (width, height) = GEOM['cube']

    def __init__(self, x: int, y: int, cube: Cube):
        super().__init__()
        self.x = x
        self.y = y
        img = pygame.image.load(DI['image']['cube'].format(repr(cube)))

        self.image = pygame.transform.scale(img, self.size)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        # self.cube = pygame.sprite.Sprite(self.image, (self.x, self.y))


    def paint(self, display: pygame.Surface):
        display.blit(self.image, (self.x, self.y))


