from cup import Cup
from table import Table
from prettytable import PrettyTable

table_game = Table()
pr_table = PrettyTable()
pr_table.add_column(" ",["Люди", "Курицы", "Коровы", "Лазеры", "Танки"])
creatures = {1: "Людей", 2: "Куриц", 3: "Коров", 4: "Лазеры смерти"}

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
            print('Вы вынужденно улетаете')
            break
        else:
            while True:
                step = int(input('Что вы хотите отложить?\n1)Людей\n2)Куриц\n3)Коров\n4)Лазеры смерти\n'))
                if step == 1:
                    if table_game.people == 0:
                        table_game.hand.numbers -= table_game.hand.people
                        table_game.people += table_game.hand.people
                        break
                    else:
                        print('Нельзя откладывать кубики с существами, которые уже отложены, попробуйте ещё раз')
    elif step == 2:
        print(table_game.hand.numbers)