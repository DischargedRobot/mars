import pygame
from settings_view import GEOM, DI
class Tableview:
    def __init__(self, width: int, height: int):
        ''' параметры игрового поля'''
        self.width = width
        self.height = height
        self.table_disp = pygame.display.set_mode((width, height))
        self.table_img = pygame.image.load(DI['image']['table'])
        self.table_disp.blit(self.table_img, (0, 0))