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
        self.cubes_group = []

    def redraw_cubes(self, cube_list = list()):
        ''' обновление изображения '''
        if len(cube_list) != 0:
            self.paint_Cube(cube_list)
        for cube in self.cubes_group:
            cube.paint(self.table.table_disp)
        pygame.display.update()

    def paint_Cube(self, cube_list: list()):
        self.cubes_group = []
        i = 0
        while len(self.cubes_group) < len(cube_list):
            cube = CubeView(random.randint(0, round(self.width-self.width*0.30)), random.randint(0,round(self.height-self.height*0.30)), cube_list[i], i)
            if cube.collidelist(self.cubes_group) == -1:
                i += 1
                self.cubes_group.append(cube)

    def redraw_step_1_cube(self, creature: str, into_plate: dict, dice_on_table):
        cubes = [self.cubes_group[i] for i in range(len(self.cubes_group)) if self.cubes_group[i].cube == creature]
        for i in range(60):
            for j in cubes:
                j.tank_motion()
                # print(j.x, j.y, j.list_cube_tanks_coordinats, j.number)
            self.table.redraw_table(into_plate)
            self.redraw_cubes()
            pygame.display.update()
        for cube_num in range(len(self.cubes_group)-1, -1, -1):
            if self.cubes_group[cube_num].cube == creature:
                self.cubes_group.remove(self.cubes_group[cube_num])
        self.table.redraw_table(into_plate)
        self.redraw_cubes()
        pygame.display.update()
    # def redraw_step_1_cube_results(self, number: int):
    # def redraw_end(self):


    def redraw(self, list_cup: dict):
        self.table.redraw_table(list_cup)
        self.table.redraw_action_of_player()
        self.table.redraw_end()
        self.redraw_cubes()
        pygame.display.update()

    def redraw_without_action_of_pl(self, list_cup: dict):
        self.table.redraw_table(list_cup)
        self.table.redraw_end()
        self.redraw_cubes()
        pygame.display.update()

    def redraw_end(self, score, text):
        self.table.table_disp.blit(self.table.table_img, (0,0))
        self.table.redraw_score(score, text)
        # self.table.redraw_continue()
        pygame.display.update()





