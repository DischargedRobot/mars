import pygame

from cup import Cup
from table import Table
from prettytable import PrettyTable
from pytest import *
from table_view import Tableview
from settings_view import GEOM
from game_view import GameView
class Game:
    size_display = (width_display, height_display) = GEOM['display']
    def __init__(self):

        self.cup = Cup()
        self.table = Table()
        self.table_view = Tableview(self.width_display, self.height_display)
        self.all_table = PrettyTable()
        self.creatures_flag = {'человек': 0, 'курица': 0, 'корова': 0, 'лазер': 0}
        self.flag = 0
        self.gameview = GameView(GEOM['display'][0], GEOM['display'][1])
        self.score_1 = 0
    def aside(self, action):
        ''' Откладывание кубиков в строну '''
        def crows():
            self.table.plate['корова'] = self.table.dice_on_table['корова']
            self.cup.numbers -= self.table.dice_on_table['корова']

        def chikens():
            self.table.plate['курица'] = self.table.dice_on_table['курица']
            self.cup.numbers -= self.table.dice_on_table['курица']

        def people():
            self.table.plate['человек'] = self.table.dice_on_table['человек']
            self.cup.numbers -= self.table.dice_on_table['человек']

        def lasers():
            self.table.plate['лазер'] += self.table.dice_on_table['лазер']
            self.cup.numbers -= self.table.dice_on_table['лазер']

        creatures_func = {'человек': people, 'курица': chikens, 'корова': crows, 'лазер': lasers} # для вызова функции
        creatures_str = {'1': "человек", '2': "курица", '3': "корова", '4': "лазер"} # для обращения к элементам стола
        flag_list = ["человек", "курица", "корова", "лазер", "танк"]
        # проверка на то, брали ли мы уже существо/лазер себе на корабль в этом ходу
        if self.table.dice_on_table[action] != 0 and self.creatures_flag[action] == 0 :
            if self.flag == 0: # если выбрали существ
                self.creatures_flag[action] = 1
                self.flag = 1 #больше брать в этом ходу существ нельзя
                creatures_func[action]()

                return True
            else:  # если попытались выбрать существ из другой группы
                print("К сожалению, мы не можем это отложить, попробуйте снова")
                return False
        else:
            print("К сожалению, мы не можем это отложить, попробуйте снова")
            return False


    def paint_all_table(self):
        ''' Отрисовка таблицы '''
        self.all_table.clear()
        self.all_table.add_column("", ["Люди", "Курицы", "Коровы", "Лазеры", "Танки"])
        self.all_table.add_column("Выпали",
                                  [self.table.dice_on_table[key] for key in self.table.dice_on_table.keys()])
        self.all_table.add_column("Уже отложены", [self.table.plate[key] for key in self.table.plate.keys()])
        print(self.all_table)


    def score(self):
        ''' подсчёт очков '''
        if self.table.dice_on_table['танк'] <= self.table.dice_on_table['лазер']:
            self.text = 'Ваше кол-во очков'
            score = self.table.plate['курица'] + self.table.plate['человек'] + self.table.plate['корова']
            if self.table.plate['курица'] != 0 and self.table.plate['человек'] != 0 and self.table.plate['корова'] != 0:
                self.score_1 += score + 3
            else:
                self.score_1 += score
        else:
            self.text = 'Вы проиграли'
    def action_1(self):
        ''' Бросок кубиков'''
        self.cup.cast()
        self.gameview.redraw_cubes(self.cup.list_cup)
        for key in list(self.table.dice_on_table.keys()):  # записываем все выпавшие значения в список стола
            self.table.dice_on_table[key] = self.cup.list_cup.count(key)
        self.table.plate['танк'] += self.cup.list_cup.count('танк')  # откладываем танки в сторону
        self.cup.numbers -= self.cup.list_cup.count('танк')  # вычитаем из кол-во кубиков кол-во танков
        self.paint_all_table()
        self.gameview.redraw_step_1_cube("танк", self.table.plate, "танк")
        self.gameview.redraw_without_action_of_pl(self.table.plate)
        while True:  # запускаем вечный цикл, пока пользователь не закончит ходить
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    test = pygame.Rect((x,y),(1,1))
                    colide = test.collidelist(self.gameview.cubes_group)
                    if colide != -1:
                        # print(self.gameview.cubes_group[colide].cube)
                        self.paint_all_table()
                        if self.aside(self.gameview.cubes_group[colide].cube):
                            self.gameview.redraw_step_1_cube(self.gameview.cubes_group[colide].cube, self.table.plate, self.table.dice_on_table)
                            self.gameview.redraw_without_action_of_pl(self.table.plate)
                            self.creatures_flag['лазер'] = 0  # обнуление флагов для следующего хода
                            self.flag = 0
                            return
                    if self.gameview.table.end.collidepoint((x, y)):
                        self.running = False
                        return
                elif event.type == pygame.QUIT:
                    self.running = False
                    return

            self.gameview.redraw_without_action_of_pl(self.table.plate)


    def step(self, action: 0):
        ''' Действия во врем хода'''
        if action == '1': # бросаем кубики

            print(self.cup.list_cup)

            self.action_1()

        elif action == '2': #просмотр содержимого стола
            print(self.all_table)
        else:
            print("Вы ввели неверное числа, повторите попытку")
    def event_process(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if self.gameview.table.action.collidepoint((x,y)):
                self.action_1()
                if self.running == False:
                    return False
            elif self.gameview.table.end.collidepoint((x, y)):
                return False
            if self.cup.numbers == 0:
                return False

    def run(self):
        self.running = True
        self.continu = True
        clock = pygame.time.Clock()
        while self.running:
            self.gameview.redraw(self.table.plate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif self.event_process(event) == False:
                    self.score()
                    while self.continu:
                        self.gameview.redraw_end(self.score_1, self.text)
                        for event_1 in pygame.event.get():
                            if event_1.type == pygame.QUIT:
                                self.continu = False
                        clock.tick(60)
            clock.tick(60)





