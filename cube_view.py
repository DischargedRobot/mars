import pygame

from settings_view import GEOM, DI
from cube import Cube

class CubeView:
    ''' отрисовка кубика'''
    size = (width, height) = GEOM['cube']

    def __init__(self, x: int, y: int, cube: Cube):
        self.x = x
        self.y = y
        self.cube = cube
        img = pygame.image.load(DI['image']['cube'].format(repr(cube)))
        self.image = pygame.transform.scale(img, self.size)

    def paint(self, display: pygame.Surface):
        display.blit(self.image, (self.x, self.y))


