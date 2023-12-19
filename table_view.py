import pygame
from settings_view import GEOM, DI
from cube import Cube
from cube_view import CubeView
pygame.init()
class Tableview:
    size_action = (width_action, height_action) = GEOM['action']
    size_cube = (width_cube, height_cube) = GEOM['cube']
    size_table = (width_display,  height_display) = GEOM['display']
    def __init__(self, width: int, height: int):

        ''' параметры игрового поля'''
        self.width = width
        self.height = height
        self.table_disp = pygame.display.set_mode((width, height))
        self.table_img = pygame.image.load(DI['image']['table'])
        self.table_disp.blit(self.table_img, (0, 0))
        self.action = pygame.Rect((self.width_display * 0.25, self.height_display - self.height_action * 1.4),
                                  (self.width_action, self.height_action))
        action_img = pygame.image.load(DI['image']['action'])
        self.action_image = pygame.transform.scale(action_img, self.size_action)
        self.end = pygame.Rect((self.width_display * 0.55, self.height_display - self.height_action * 1.4),
                                  (self.width_action, self.height_action))
        end_img = pygame.image.load(DI['image']['end'])
        self.end_image = pygame.transform.scale(end_img, self.size_action)

    def redraw_table(self, list_creature: dict ):
        self.table_disp.blit(self.table_img, (0,0))
        creatures = ['человек', 'курица', 'корова', 'лазер', 'танк']
        cubes_view = [CubeView(self.width_display*0.74+self.width_cube, self.height_cube*1.5*i, creatures[i-1], 1) for i in range(1,6)]
        for cube_view in cubes_view:
            cube_view.paint(self.table_disp)
        cubes_number_font = pygame.font.SysFont('Times New Roman', 24)
        # print(list_creature, 'sadas')
        cubes_number_text = [cubes_number_font.render(f'x {str(list_creature[creatures[i]])}', True, 'White') for i in range(5)]
        for i in range(1,6):
            self.table_disp.blit(cubes_number_text[i-1], (self.width_display*0.74+self.width_cube*2, self.height_cube*1.5*i))
        # img = pygame.image.load(DI['image']['cube'].format(cubes[5]))
        # img_cube = pygame.transform.scale(img, self.size_cube)
        # CubeView(self.width, self.height).paint(self.table_disp)

    def redraw_action_of_player(self):
        self.table_disp.blit(self.action_image, (self.width_display*0.25, self.height_display - self.height_action*1.4))

    def redraw_end(self):
        self.table_disp.blit(self.end_image, (self.width_display*0.50,self.height_display - self.height_action*1.4))

    def redraw_score(self, score, text):
        number_score_fonr = pygame.font.SysFont('Times New Roman', 24)
        # print(list_creature, 'sadas')
        number_score_text = number_score_fonr.render(f' {text} {str(score)}', True, 'White')
        self.table_disp.blit(number_score_text,(self.width_display * 0.50 - number_score_text.get_width()*0.5, self.height_display * 0.5 - number_score_text.get_height()))

    def redraw_continue(self):
        self.contiue = pygame.Rect(
            (self.width_display * 0.50 - self.width_action * 0.5, self.height_display * 0.5 - self.height_action),
            (self.width_action, self.height_action))
        continue_img = pygame.image.load(DI['image']['action'])
        self.contiue_image = pygame.transform.scale(continue_img, self.size_action)
        self.table_disp.blit(self.contiue_image,
                             (self.width_display * 0.25, self.height_display - self.height_action * 1.4))