import pygame

from cup import Cup
from table import Table
from prettytable import PrettyTable
from pytest import *
from settings_view import GEOM
from game_view import GameView
class Game:
    def __init__(self):
        self.cup = Cup()
        self.table = Table()
        self.all_table = PrettyTable()
        self.creatures_flag = {'1': 0, '2': 0, '3': 0, '4': 0}
        self.flag = 0
        self.gameview = GameView(GEOM['display'][0], GEOM['display'][1])
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

        creatures_func = {'1': people, '2': chikens, '3': crows, '4': lasers} # для вызова функции
        creatures_str = {'1': "человек", '2': "курица", '3': "корова", '4': "лазер"} # для обращения к элементам стола

        # проверка на то, брали ли мы уже существо/лазер себе на корабль в этом ходу
        if self.table.dice_on_table[creatures_str[action]] != 0 and self.creatures_flag[action] == 0 :
            if action != "4" and self.flag == 0: # если выбрали существ
                self.creatures_flag[action] = 1
                self.flag = 1 #больше брать в этом ходу существ нельзя
                creatures_func[action]()
                return True
            elif action == '4':  #если выбрали лазер
                self.creatures_flag['4'] = 1
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
        score = self.table.plate['курица'] + self.table.plate['человек'] + self.table.plate['корова']
        if self.table.plate['курица'] != 0 and  self.table.plate['человек'] != 0 and self.table.plate['корова'] != 0:
            return score + 3
        return score

    def action_1(self):
        ''' Бросок кубиков'''
        for key in list(self.table.dice_on_table.keys()):  # записываем все выпавшие значения в список стола
            self.table.dice_on_table[key] = self.cup.list_cup.count(key)
        self.table.plate['танк'] += self.cup.list_cup.count('танк')  # откладываем танки в сторону
        self.cup.numbers -= self.cup.list_cup.count('танк')  # вычитаем из кол-во кубиков кол-во танков
        self.paint_all_table()
        while True:  # запускаем вечный цикл, пока пользователь не закончит ходить
            flag = input(
                'Что вы хотите сделать?\n1)Забрать людей\n2)Забрать куриц\n3)Забрать коров\n4)Забрать лазеры\n5)Закончить ход\n')
            if flag == '5':
                break
            self.aside(flag)
            self.paint_all_table()
        self.creatures_flag['4'] = 0  # обнуление флагов для следующего хода
        self.flag = 0
    def step(self, action: 0):
        ''' Действия во врем хода'''
        if action == '1': # бросаем кубики
            self.cup.cast()
            self.gameview.redraw_table()
            self.gameview.redraw_cubes(self.cup.list_cup)
            self.action_1()
        elif action == '2': #просмотр содержимого стола
            print(self.all_table)
        else:
            print("Вы ввели неверное числа, повторите попытку")
    # def run(self):
    #     running = True
    #     while running:
    #     self.gameview.redraw_cubes()
