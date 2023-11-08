from cup import Cup
from table import Table
from prettytable import PrettyTable

table_game = Table()
def people_1():
    if table_game.people == 0:
        table_game.hand.numbers -= table_game.hand.people
        table_game.people += table_game.hand.people
        return True
    return False

def chiken_1():
    if table_game.chiken == 0:
        table_game.hand.numbers -= table_game.hand.chiken
        table_game.chiken += table_game.hand.chiken
        return True
    return False
def cow_1():
    if table_game.cow == 0:
        table_game.hand.numbers -= table_game.hand.cow
        table_game.cow += table_game.hand.cow
        return True
    return False
def laser_1():
    table_game.hand.numbers -= table_game.hand.laser
    table_game.laser += table_game.hand.laser
    return True

pr_table = PrettyTable()
pr_table.add_column(" ",["Люди", "Курицы", "Коровы", "Лазеры", "Танки"])
creatures = {1: people_1, 2: chiken_1, 3: cow_1, 4: laser_1}
while True:
    step = int(input('Ващи действия?\n1) Бросить кубики\n2) Посмотреть количество кубиков\n'))
    if step == 1:
        table_game.put_aside()
        pr_table.add_column("Выпавшие кубики",
                            [table_game.hand.people, table_game.hand.chiken, table_game.hand.cow, table_game.hand.laser,
                             table_game.hand.tank])
        pr_table.add_column("Отобранные кубики",
                            [table_game.people, table_game.chiken, table_game.cow, table_game.laser, table_game.tank])
        print(pr_table)
        pr_table.del_column("Выпавшие кубики")
        pr_table.del_column("Отобранные кубики")
        if table_game.tank > table_game.hand.numbers:
            print('Вы в спешке вынужденно улетаете, потеряв груз')
            break
        else:
            while True:
                step = int(input('Что вы хотите отложить?\n1)Людей\n2)Куриц\n3)Коров\n4)Лазеры смерти\n5)Ничего не хочу, перебрасываю\n'))
                if (creatures[step]() == True) and (step != 4):
                    break
                elif creatures[step]() == False:
                    print('Нельзя откладывать кубики с существами, которые уже отложены, попробуйте ещё раз')


    elif step == 2:
        print(table_game.hand.numbers)